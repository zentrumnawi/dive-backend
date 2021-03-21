from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class ArrayMultipleChoiceField(forms.MultipleChoiceField):
    def __init__(self, model=None, field_name="", **kwargs):
        if model and field_name:
            _label = model._meta.get_field(field_name).base_field.verbose_name
        else:
            _label = None

        required = kwargs.pop("required", False)
        label = kwargs.pop("label", _label)

        super().__init__(required=required, label=label, **kwargs)


class IntegerRangeCharWidget(forms.MultiWidget):
    def __init__(self, min, max, attrs=None):
        self.max = max
        widgets = (
            forms.NumberInput(attrs={"min": min, "max": max}),
            forms.NumberInput(attrs={"min": min, "max": max}),
        )
        super().__init__(widgets, attrs=attrs)

    def decompress(self, value):
        if value:
            return [self.max if v == "∞" else v for v in value.split("–", 1)]
        return [None, None]


class IntegerRangeCharField(forms.MultiValueField):
    def __init__(
        self, min=1, max=99, infinity=False, model=None, field_name="", **kwargs
    ):
        self.max = max
        self.infinity = infinity
        _label = None
        if model and field_name:
            _label = model._meta.get_field(field_name).verbose_name
        _help_text = "Einzelwert oder Wertebereich"
        if infinity:
            _help_text += f", {max} wird als ∞ gespeichert."
        kwargs.setdefault("required", False)
        kwargs.setdefault("label", _label)
        kwargs.setdefault("help_text", _help_text)

        fields = (
            forms.IntegerField(
                min_value=min,
                max_value=max,
                error_messages={
                    "min_value": "Ensure first value is greater than or equal to %(limit_value)s.",
                    "max_value": "Ensure first value is less than or equal to %(limit_value)s.",
                },
            ),
            forms.IntegerField(
                min_value=min,
                max_value=max,
                error_messages={
                    "min_value": "Ensure second value is greater than or equal to %(limit_value)s.",
                    "max_value": "Ensure second value is less than or equal to %(limit_value)s.",
                },
            ),
        )
        widget = IntegerRangeCharWidget(min, max)

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

        data = "–".join(filter(None, data_list))

        return data
