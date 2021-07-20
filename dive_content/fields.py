from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from .choices import INDICATORS, INDICATORS_CHOICES, SEASON_CHOICES
from .models import Indicators
from .widgets import (
    IndicatorWidget,
    NumberRangeCharWidget,
    NumberRangeCharWidget_to_be_deleted,
    NumericPrefixTermWidget,
    OutputWidget,
    SeasonWidget,
)


class AdaptedSimpleArrayField(SimpleArrayField):
    def prepare_value(self, value):
        return value


class ArrayMultipleChoiceField(forms.MultipleChoiceField):
    def __init__(self, choices, **kwargs):
        kwargs.setdefault("required", False)

        super().__init__(choices=choices, **kwargs)


class IndicatorField(forms.MultiValueField):
    def __init__(self, field_name, **kwargs):
        choices = INDICATORS_CHOICES[INDICATORS.index(field_name)]
        self.mode = field_name
        kwargs.setdefault("required", False)
        kwargs.setdefault("label", Indicators._meta.get_field(field_name).verbose_name)
        if not kwargs["required"] and not any(
            key in (None, "") for key in dict(choices).keys()
        ):
            choices = (("", "---------"),) + choices

        fields = [
            forms.ChoiceField(choices=choices),
            forms.BooleanField(),
        ]
        if self.mode == "light":
            fields.append(forms.BooleanField())
        if self.mode == "humidity":
            fields.extend([forms.BooleanField()] * 2)
        widget = IndicatorWidget(choices, self.mode)

        super().__init__(fields=fields, widget=widget, **kwargs)

    def compress(self, data_list):
        error_message = _("Non-numeric values must not have additional symbols.")
        if data_list[0][1:2] in ("x", "?") and (
            data_list[-1]
            or (self.mode == "light" and data_list[1])
            or (self.mode == "humidity" and (data_list[1] or data_list[2]))
        ):
            raise ValidationError(error_message)

        value = f"{f'{data_list[0]}' if data_list[0] else ''}"
        if self.mode == "light":
            value = f"{f'{value}()' if value and data_list[1] else f'{value}'}"
        if self.mode == "humidity":
            value = f"{f'{value}~' if value and data_list[1] else f'{value}'}"
            value = f"{f'{value}=' if value and data_list[2] else f'{value}'}"
        value = f"{f'{value} (?)' if value and data_list[-1] else f'{value}'}"

        return value


class IntegerRangeCharField(forms.MultiValueField):
    help_text = "Einzelwert oder Wertebereich"
    field = forms.IntegerField
    widget = NumberRangeCharWidget

    def __init__(self, min, max, substitutes={}, **kwargs):
        self.substitutes = substitutes
        reversed_substitutes = {}
        if substitutes:
            reversed_substitutes = {v: k for k, v in substitutes.items()}
            for k, v in substitutes.items():
                self.help_text += f', {k}="{v}"'

        kwargs.setdefault("required", False)
        kwargs.setdefault("help_text", self.help_text)

        def error_messages(position):
            return {
                "min_value": f"Ensure {position} value is greater than or equal to %(limit_value)s.",
                "max_value": f"Ensure {position} value is less than or equal to %(limit_value)s.",
            }

        field_1_kwargs = {
            "min_value": min,
            "max_value": max,
            "error_messages": error_messages("first"),
        }
        field_2_kwargs = dict(field_1_kwargs)
        field_2_kwargs.update({"error_messages": error_messages("second")})

        fields = (self.field(**field_1_kwargs), self.field(**field_2_kwargs))
        widget = self.widget(min, max, reversed_substitutes)

        super().__init__(fields=fields, widget=widget, **kwargs)

    def compress(self, data_list):
        if len(data_list) > 1 and all(data_list):
            if data_list[0] > data_list[1]:
                raise ValidationError(_("First value must not exceed second value."))
            if data_list[0] == data_list[1]:
                data_list[1] = None

        for i, data in enumerate(data_list):
            if data is not None:
                data_list[i] = str(data)
                if self.substitutes:
                    if data in self.substitutes:
                        data_list[i] = self.substitutes[data]

        return "–".join(filter(None, data_list))


class FloatRangeCharField(IntegerRangeCharField):
    field = forms.FloatField


class NumberRangeCharField_to_be_replaced(forms.MultiValueField):
    def __init__(self, min=1, max=99, suffix=None, infinity=False, **kwargs):
        self.max = max
        self.infinity = infinity
        help_text = "Einzelwert oder Wertebereich"
        if infinity:
            help_text += f", {max} wird als ∞ gespeichert."
        kwargs.setdefault("required", False)
        kwargs.setdefault("help_text", help_text)

        def error_messages(pos):
            position = {1: "first", 2: "second"}
            return {
                "min_value": f"Ensure {position[pos]} value is greater than or equal to %(limit_value)s.",
                "max_value": f"Ensure {position[pos]} value is less than or equal to %(limit_value)s.",
            }

        fields = (
            forms.IntegerField(
                min_value=min, max_value=max, error_messages=error_messages(1)
            ),
            forms.IntegerField(
                min_value=min, max_value=max, error_messages=error_messages(2)
            ),
        )
        widget = NumberRangeCharWidget_to_be_deleted(min, max)
        if suffix == "cm":
            fields = (
                forms.FloatField(
                    min_value=min, max_value=max, error_messages=error_messages(1)
                ),
                forms.FloatField(
                    min_value=min, max_value=max, error_messages=error_messages(2)
                ),
            )
            widget = NumberRangeCharWidget_to_be_deleted(min, max, 0.1, "cm")

        super().__init__(fields=fields, widget=widget, **kwargs)

    def compress(self, data_list):
        if len(data_list) > 1 and all(data_list):
            if data_list[0] > data_list[1]:
                raise ValidationError(_("First value must not exceed second value."))
            if data_list[0] == data_list[1]:
                data_list[1] = None

        for i, data in enumerate(data_list):
            if data:
                data_list[i] = str(data)
                if self.infinity and data == self.max:
                    data_list[i] = "∞"

        return "–".join(filter(None, data_list))


class NumericPrefixTermField(forms.MultiValueField):
    def __init__(self, choices, **kwargs):
        kwargs.setdefault("required", False)

        fields = [
            forms.ChoiceField(choices=choices[0]),
            forms.ChoiceField(choices=choices[1]),
        ]
        widget = NumericPrefixTermWidget(choices)

        super().__init__(fields=fields, widget=widget, **kwargs)

    def compress(self, data_list):
        value = ""
        if data_list:
            if not data_list[0] and len(data_list[1]) == 2:
                raise ValidationError(_("Numeric prefix must be provided."))
            value = "".join(data_list) if len(data_list[1]) == 2 else data_list[1]

        return value


class OutputField(forms.Field):
    def __init__(self, output=None):
        super().__init__(
            required=False,
            widget=OutputWidget,
            label="",
            initial=output,
            label_suffix="",
        )


class SeasonField(forms.MultiValueField):
    def __init__(self, **kwargs):
        kwargs.setdefault("required", False)
        kwargs.setdefault("help_text", _("Einzelwert in Feld 2 eintragen."))

        choices = SEASON_CHOICES
        fields = [
            forms.TypedChoiceField(choices=choices, coerce=int, empty_value=None)
        ] * 4
        widget = SeasonWidget(choices)

        super().__init__(fields=fields, widget=widget, **kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] and not data_list[1] or data_list[0] == data_list[1]:
                data_list[0] = None
            if data_list[3] and not data_list[2] or data_list[3] == data_list[2]:
                data_list[3] = None
            if (data_list.count(None) == 3 and data_list[2]) or (
                data_list.count(None) == 2 and data_list[2] == data_list[1]
            ):
                data_list[1] = data_list[2]
                data_list[2] = None

        return data_list


class SubsectionTitleField(forms.Field):
    def __init__(self, title, color="#2f7692"):
        label = format_html(f'<span style="color:{color};"><b>{title}</b></span>')
        super().__init__(required=False, label=label, label_suffix="")
        self.widget.attrs = {"style": "display:none;"}
