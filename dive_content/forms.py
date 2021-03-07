from django import forms

from .choices import *
from .models import Leaf, Plant


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
    att_axis = forms.MultipleChoiceField(
        choices=AXIS_CHOICES,
        required=False,
        label=Leaf._meta.get_field("att_axis").base_field.verbose_name,
    )
