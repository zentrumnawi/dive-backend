from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .choices import *
from .fields import (
    ArrayMultipleChoiceField,
    ConnationTypeField,
    IndicatorField,
    NumberRangeCharField,
    SeasonField,
)
from .models import Blossom, Fruit, Leaf, Plant, StemRoot


def get_label(model, field_name):
    label = model._meta.get_field(field_name).verbose_name
    if isinstance(model._meta.get_field(field_name), ArrayField):
        label = model._meta.get_field(field_name).base_field.verbose_name

    return label


class PlantAdminForm(forms.ModelForm):
    habitat = forms.MultipleChoiceField(
        choices=Plant.HABITAT_CHOICES,
        required=False,
        label=get_label(Plant, "habitat"),
    )
    ground = forms.MultipleChoiceField(
        choices=Plant.GROUND_CHOICES, required=False, label=get_label(Plant, "ground")
    )


class LeafAdminForm(forms.ModelForm):
    attachment = ArrayMultipleChoiceField(ATTACHMENT_CHOICES, Leaf, "attachment")
    leaf_comp_blade_shape = ArrayMultipleChoiceField(
        LEAF_COMP_BLADE_SHAPE_CHOICES, Leaf, "leaf_comp_blade_shape"
    )
    leaf_comp_incision_depth = ArrayMultipleChoiceField(
        LEAF_COMP_INCISION_DEPTH_CHOICES, Leaf, "leaf_comp_incision_depth"
    )
    leaflet_incision_depth = ArrayMultipleChoiceField(
        LEAFLET_INCISION_DEPTH_CHOICES, Leaf, "leaflet_incision_depth"
    )
    leaf_simple_blade_shape = ArrayMultipleChoiceField(
        LEAF_SIMPLE_BLADE_SHAPE_CHOICES, Leaf, "leaf_simple_blade_shape"
    )
    leaf_simple_incision_depth = ArrayMultipleChoiceField(
        LEAF_SIMPLE_INCISION_DEPTH_CHOICES, Leaf, "leaf_simple_incision_depth"
    )
    edge = ArrayMultipleChoiceField(EDGE_CHOICES, Leaf, "edge")
    surface = ArrayMultipleChoiceField(SURFACE_CHOICES, Leaf, "surface")
    stipule_edge = ArrayMultipleChoiceField(STIPULE_EDGE_CHOICES, Leaf, "stipule_edge")

    leaf_comp_num = NumberRangeCharField(Leaf, "leaf_comp_num")
    leaf_comp_incision_num = NumberRangeCharField(Leaf, "leaf_comp_incision_num")
    leaflet_incision_num = NumberRangeCharField(Leaf, "leaflet_incision_num")
    leaf_simple_num = NumberRangeCharField(Leaf, "leaf_simple_num")
    leaf_simple_incision_num = NumberRangeCharField(Leaf, "leaf_simple_incision_num")


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

    def clean_bract_blade(self):
        choices = BRACT_BLADE_CHOICES
        sublists = (LEAF_COMP_BLADE_SHAPE_CHOICES, LEAF_SIMPLE_BLADE_SHAPE_CHOICES)
        value = self.cleaned_data.get("bract_blade")

        error_messages = {
            "invalid_choice": _(
                f"Only first {len(sublists[0])} or following {len(sublists[1])} options may be selected together."
            ),
            "multiple_choice_not_allowed": _(
                f'Option "{dict(choices).get("nvo")}" may only be selected alone.'
            ),
        }
        if any(v in dict(sublists[0]).keys() for v in value) and any(
            v in dict(sublists[1]).keys() for v in value
        ):
            raise ValidationError(error_messages["invalid_choice"])
        if choices[-1][0] in value and len(value) > 1:
            raise ValidationError(error_messages["multiple_choice_not_allowed"])

        return value

    def save(self, commit=True):
        # Clear blossom_num if option "Einzelblüte" is selected as inflorescence_type.
        instance = super().save(commit=False)

        inflorescence_type = self.cleaned_data.get("inflorescence_type", "")
        blossom_num = self.cleaned_data.get("blossom_num", "")
        if inflorescence_type == "ein" and blossom_num:
            instance.blossom_num = ""

        if commit:
            instance.save()

        return instance


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
