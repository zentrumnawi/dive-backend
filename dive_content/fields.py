from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .choices import INDICATORS, INDICATORS_CHOICES, SEASON_CHOICES
from .models import Blossom, Indicators
from .widgets import IndicatorWidget, NumberRangeCharWidget, SeasonWidget


class ArrayMultipleChoiceField(forms.MultipleChoiceField):
    def __init__(self, choices, model=None, field_name=None, **kwargs):
        _label = None
        if model and field_name:
            _label = model._meta.get_field(field_name).base_field.verbose_name
        kwargs.setdefault("required", False)
        kwargs.setdefault("label", _label)

        super().__init__(choices=choices, **kwargs)


class NumberRangeCharField(forms.MultiValueField):
    def __init__(
        self,
        model=None,
        field_name=None,
        min=1,
        max=99,
        suffix=None,
        infinity=False,
        **kwargs,
    ):
        _label = None
        if model and field_name:
            _label = model._meta.get_field(field_name).verbose_name
        _help_text = "Einzelwert oder Wertebereich"
        self.max = max
        self.infinity = infinity
        if infinity:
            _help_text += f", {max} wird als ∞ gespeichert."
        kwargs.setdefault("required", False)
        kwargs.setdefault("label", _label)
        kwargs.setdefault("help_text", _help_text)

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
        widget = NumberRangeCharWidget(min, max)
        if suffix == "cm":
            fields = (
                forms.FloatField(
                    min_value=min, max_value=max, error_messages=error_messages(1)
                ),
                forms.FloatField(
                    min_value=min, max_value=max, error_messages=error_messages(2)
                ),
            )
            widget = NumberRangeCharWidget(min, max, 0.1, "cm")

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


class SeasonField(forms.MultiValueField):
    def __init__(self, field_name, **kwargs):
        kwargs.setdefault("required", False)
        kwargs.setdefault(
            "label", Blossom._meta.get_field(field_name).base_field.verbose_name
        )
        kwargs.setdefault("help_text", _("Einzelwert in Feld 2 oder 3 eintragen."))

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

        return data_list


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
