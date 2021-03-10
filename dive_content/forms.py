from django import forms

from .choices import *
from .models import Leaf, Plant


class ArrayMultipleChoiceField(forms.MultipleChoiceField):
    def __init__(self, model, array_field_name, *args, **kwargs):
        required = kwargs.pop("required", False)
        label = kwargs.pop(
            "label", model._meta.get_field(array_field_name).base_field.verbose_name,
        )
        super().__init__(*args, required=required, label=label, **kwargs)


class PlantAdminForm(forms.ModelForm):
    habitat = forms.MultipleChoiceField(
        choices=Plant.HABITAT_CHOICES,
        required=False,
        label=Plant._meta.get_field("habitat").base_field.verbose_name,
    )
    ground = forms.MultipleChoiceField(
        choices=Plant.GROUND_CHOICES,
        required=False,
        label=Plant._meta.get_field("ground").base_field.verbose_name,
    )


class LeafAdminForm(forms.ModelForm):
    att_axis = ArrayMultipleChoiceField(Leaf, "att_axis", choices=AXIS_CHOICES)
    dep_cuts = ArrayMultipleChoiceField(Leaf, "dep_cuts", choices=CUT_CHOICES)
    blade_div = ArrayMultipleChoiceField(Leaf, "blade_div", choices=BLADE_DIV_CHOICES)
    blade_undiv = ArrayMultipleChoiceField(
        Leaf, "blade_undiv", choices=BLADE_UNDIV_CHOICES
    )
    margin = ArrayMultipleChoiceField(Leaf, "margin", choices=MARGIN_CHOICES)
    surface = ArrayMultipleChoiceField(Leaf, "surface", choices=SURFACE_CHOICES)
    stipule_margin = ArrayMultipleChoiceField(
        Leaf, "stipule_margin", choices=MARGIN_CHOICES
    )
