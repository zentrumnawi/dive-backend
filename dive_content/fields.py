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
    def __init__(self, attrs=None):
        widgets = (
            forms.NumberInput(attrs={"min": 1, "max": 99}),
            forms.NumberInput(attrs={"min": 1, "max": 99}),
        )
        super().__init__(widgets, attrs=attrs)

    def decompress(self, value):
        if value:
            return value.split("-", 1)
        return [None, None]


class IntegerRangeCharField(forms.MultiValueField):
    def __init__(self, model=None, field_name="", **kwargs):
        _label = None
        if model and field_name:
            _label = model._meta.get_field(field_name).verbose_name
        kwargs.setdefault("required", False)
        kwargs.setdefault("label", _label)
        kwargs.setdefault("help_text", "Einzelwert oder Wertebereich")

        fields = (
            forms.IntegerField(
                min_value=1,
                max_value=99,
                error_messages={
                    "min_value": "Ensure first value is greater than or equal to %(limit_value)s.",
                    "max_value": "Ensure first value is less than or equal to %(limit_value)s.",
                },
            ),
            forms.IntegerField(
                min_value=1,
                max_value=99,
                error_messages={
                    "min_value": "Ensure second value is greater than or equal to %(limit_value)s.",
                    "max_value": "Ensure second value is less than or equal to %(limit_value)s.",
                },
            ),
        )
        widget = IntegerRangeCharWidget

        super().__init__(fields=fields, widget=widget, **kwargs)

    def compress(self, data_list):
        if len(data_list) > 1 and all(data_list):
            if data_list[0] > data_list[1]:
                raise ValidationError(_("First value must not exceed second value."))
            if data_list[0] == data_list[1]:
                data_list[1] = None
        data = "-".join(filter(None, [str(i) if i else "" for i in data_list]))

        return data
