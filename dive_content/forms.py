from django import forms

from .choices import *
from .models import Leaf, Plant


class ArrayMultipleChoiceField(forms.MultipleChoiceField):
    def __init__(self, model=None, field_name="", **kwargs):
        if model and field_name:
            _label = model._meta.get_field(field_name).base_field.verbose_name
        else:
            _label = None

        required = kwargs.pop("required", False)
        label = kwargs.pop("label", _label)

        super().__init__(required=required, label=label, **kwargs)


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
    attachment = ArrayMultipleChoiceField(
        Leaf, "attachment", choices=ATTACHMENT_CHOICES
    )
    blade_subdiv_shape = ArrayMultipleChoiceField(
        Leaf, "blade_subdiv_shape", choices=BLADE_SUBDIV_SHAPE_CHOICES
    )
    incision_depth = ArrayMultipleChoiceField(
        Leaf, "incision_depth", choices=INCISION_DEPTH_CHOICES
    )
    blade_undiv_shape = ArrayMultipleChoiceField(
        Leaf, "blade_undiv_shape", choices=BLADE_UNDIV_SHAPE_CHOICES
    )
    leaflet_incision_depth = ArrayMultipleChoiceField(
        Leaf, "leaflet_incision_depth", choices=LEAFLET_INCISION_DEPTH_CHOICES
    )
    edge = ArrayMultipleChoiceField(Leaf, "edge", choices=EDGE_CHOICES)
    surface = ArrayMultipleChoiceField(Leaf, "surface", choices=SURFACE_CHOICES)
    stipule_edge = ArrayMultipleChoiceField(Leaf, "stipule_edge", choices=EDGE_CHOICES)
