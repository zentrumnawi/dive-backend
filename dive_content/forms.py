from django import forms

from .choices import *
from .fields import (
    ArrayMultipleChoiceField,
    ConnationTypeField,
    IndicatorField,
    NumberRangeCharField,
    SeasonField,
)
from .models import Blossom, Fruit, Leaf, Plant, StemRoot


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

    leaf_comp_num = NumberRangeCharField(Leaf, "leaf_comp_num")
    incision_num = NumberRangeCharField(Leaf, "incision_num")
    leaflet_incision_num = NumberRangeCharField(Leaf, "leaflet_incision_num")
    leaf_simple_num = NumberRangeCharField(Leaf, "leaf_simple_num")


class BlossomAdminForm(forms.ModelForm):
    season = SeasonField("season")
    inflorescence_num = NumberRangeCharField(
        Blossom, "inflorescence_num", max=100, infinity=True
    )
    blossom_num = NumberRangeCharField(Blossom, "blossom_num", max=100, infinity=True)
    bract_blade = ArrayMultipleChoiceField(BRACT_BLADE_CHOICES, Blossom, "bract_blade")
    diameter = NumberRangeCharField(Blossom, "diameter", 0.1, 100, "cm")
    sepal_num = NumberRangeCharField(Blossom, "sepal_num", max=11, infinity=True)
    sepal_connation_type = ConnationTypeField("sepal_connation_type")
    petal_num = NumberRangeCharField(Blossom, "petal_num", max=11, infinity=True)
    petal_len = NumberRangeCharField(Blossom, "petal_len", 0.1, 100, "cm")
    petal_connation_type = ConnationTypeField("petal_connation_type")
    stamen_num = NumberRangeCharField(Blossom, "stamen_num", max=11, infinity=True)
    stamen_len = NumberRangeCharField(Blossom, "stamen_len", 0.1, 100, "cm")
    carpel_num = NumberRangeCharField(Blossom, "carpel_num", max=11, infinity=True)
    stigma_num = NumberRangeCharField(Blossom, "stigma_num", max=11, infinity=True)


class FruitAdminForm(forms.ModelForm):
    seed_num = NumberRangeCharField(Fruit, "seed_num", max=100, infinity=True)


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
