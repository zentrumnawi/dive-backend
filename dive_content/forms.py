from django import forms

from .choices import *
from .fields import ArrayMultipleChoiceField, IntegerRangeCharField, IndicatorField
from .models import Fruit, Leaf, Plant, StemRoot


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
    attachment = ArrayMultipleChoiceField(ATTACHMENT_CHOICES, Leaf, "attachment")
    blade_subdiv_shape = ArrayMultipleChoiceField(
        BLADE_SUBDIV_SHAPE_CHOICES, Leaf, "blade_subdiv_shape"
    )
    incision_depth = ArrayMultipleChoiceField(
        INCISION_DEPTH_CHOICES, Leaf, "incision_depth"
    )
    blade_undiv_shape = ArrayMultipleChoiceField(
        BLADE_UNDIV_SHAPE_CHOICES, Leaf, "blade_undiv_shape"
    )
    leaflet_incision_depth = ArrayMultipleChoiceField(
        LEAFLET_INCISION_DEPTH_CHOICES, Leaf, "leaflet_incision_depth"
    )
    edge = ArrayMultipleChoiceField(EDGE_CHOICES, Leaf, "edge")
    surface = ArrayMultipleChoiceField(SURFACE_CHOICES, Leaf, "surface")
    stipule_edge = ArrayMultipleChoiceField(STIPULE_EDGE_CHOICES, Leaf, "stipule_edge")

    leaf_comp_num = IntegerRangeCharField(model=Leaf, field_name="leaf_comp_num")
    incision_num = IntegerRangeCharField(model=Leaf, field_name="incision_num")
    leaflet_incision_num = IntegerRangeCharField(
        model=Leaf, field_name="leaflet_incision_num"
    )
    leaf_simple_num = IntegerRangeCharField(model=Leaf, field_name="leaf_simple_num")


class FruitAdminForm(forms.ModelForm):
    seed_num = IntegerRangeCharField(
        max=100, infinity=True, model=Fruit, field_name="seed_num"
    )


class StemRootAdminForm(forms.ModelForm):
    orientation = ArrayMultipleChoiceField(ORIENTATION_CHOICES, StemRoot, "orientation")
    appearance = ArrayMultipleChoiceField(
        APPEARANCE_CHOICES, StemRoot, "appearance", widget=forms.CheckboxSelectMultiple
    )
    cross_section = ArrayMultipleChoiceField(
        SR_CROSS_SECTION_CHOICES, StemRoot, "cross_section"
    )
    surface = ArrayMultipleChoiceField(SURFACE_CHOICES, StemRoot, "surface")


class IndicatorsAdminForm(forms.ModelForm):
    light = IndicatorField("light")
    temperature = IndicatorField("temperature")
    humidity = IndicatorField("humidity")
    reaction = IndicatorField("reaction")
    nitrogen = IndicatorField("nitrogen")

    def save(self, commit=True):
        # Populate key field.
        indicators_values = [self.cleaned_data.get(i, "") for i in INDICATORS]
        symbols = [
            "()" in indicators_values[0],
            any("(?)" in value for value in indicators_values[:2]),  # Ensure key order.
            "~" in indicators_values[2],
            "=" in indicators_values[2],
            any("(?)" in value for value in indicators_values[2:]),  # Ensure key order.
        ]

        instance = super().save(commit=False)
        instance.key = []
        for i, symbol in enumerate(symbols):
            if symbol:
                if i == 4:
                    if not symbols[1]:
                        instance.key.append(KEY_CHOICES[1][0])
                else:
                    instance.key.append(KEY_CHOICES[i][0])

        if commit:
            instance.save()

        return instance
