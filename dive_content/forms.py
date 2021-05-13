from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .choices import *
from .fields import (
    ArrayMultipleChoiceField,
    IndicatorField,
    NumberRangeCharField_to_be_replaced,
    NumericPrefixTermField,
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
    attachment = ArrayMultipleChoiceField(
        ATTACHMENT_CHOICES, label=get_label(Leaf, "attachment")
    )
    leaf_comp_blade_shape = ArrayMultipleChoiceField(
        LEAF_COMP_BLADE_SHAPE_CHOICES, label=get_label(Leaf, "leaf_comp_blade_shape")
    )
    leaf_comp_incision_depth = ArrayMultipleChoiceField(
        LEAF_COMP_INCISION_DEPTH_CHOICES,
        label=get_label(Leaf, "leaf_comp_incision_depth"),
    )
    leaflet_incision_depth = ArrayMultipleChoiceField(
        LEAFLET_INCISION_DEPTH_CHOICES, label=get_label(Leaf, "leaflet_incision_depth")
    )
    leaf_simple_blade_shape = ArrayMultipleChoiceField(
        LEAF_SIMPLE_BLADE_SHAPE_CHOICES,
        label=get_label(Leaf, "leaf_simple_blade_shape"),
    )
    leaf_simple_incision_depth = ArrayMultipleChoiceField(
        LEAF_SIMPLE_INCISION_DEPTH_CHOICES,
        label=get_label(Leaf, "leaf_simple_incision_depth"),
    )
    edge = ArrayMultipleChoiceField(EDGE_CHOICES, label=get_label(Leaf, "edge"))
    surface = ArrayMultipleChoiceField(
        SURFACE_CHOICES, label=get_label(Leaf, "surface")
    )
    stipule_edge = ArrayMultipleChoiceField(
        STIPULE_EDGE_CHOICES, label=get_label(Leaf, "stipule_edge")
    )

    leaf_comp_num = NumberRangeCharField_to_be_replaced(
        label=get_label(Leaf, "leaf_comp_num")
    )
    leaf_comp_incision_num = NumberRangeCharField_to_be_replaced(
        label=get_label(Leaf, "leaf_comp_incision_num")
    )
    leaflet_incision_num = NumberRangeCharField_to_be_replaced(
        label=get_label(Leaf, "leaflet_incision_num")
    )
    leaf_simple_num = NumberRangeCharField_to_be_replaced(
        label=get_label(Leaf, "leaf_simple_num")
    )
    leaf_simple_incision_num = NumberRangeCharField_to_be_replaced(
        label=get_label(Leaf, "leaf_simple_incision_num")
    )


class BlossomAdminForm(forms.ModelForm):
    season = SeasonField("season")
    inflorescence_num = NumberRangeCharField_to_be_replaced(
        max=100, infinity=True, label=get_label(Blossom, "inflorescence_num")
    )
    blossom_num = NumberRangeCharField_to_be_replaced(
        max=100, infinity=True, label=get_label(Blossom, "blossom_num")
    )
    bract_blade = ArrayMultipleChoiceField(
        BRACT_BLADE_CHOICES, label=get_label(Blossom, "bract_blade")
    )
    diameter = NumberRangeCharField_to_be_replaced(
        0.1, 100, "cm", label=get_label(Blossom, "diameter")
    )
    sepal_num = NumberRangeCharField_to_be_replaced(
        max=11, infinity=True, label=get_label(Blossom, "sepal_num")
    )
    sepal_connation_type = NumericPrefixTermField(
        (CONNATION_NUM_CHOICES, CONNATION_TYPE_CHOICES),
        label=get_label(Blossom, "sepal_connation_type"),
    )
    petal_num = NumberRangeCharField_to_be_replaced(
        max=11, infinity=True, label=get_label(Blossom, "petal_num")
    )
    petal_len = NumberRangeCharField_to_be_replaced(
        0.1, 100, "cm", label=get_label(Blossom, "petal_len")
    )
    petal_connation_type = NumericPrefixTermField(
        (CONNATION_NUM_CHOICES, CONNATION_TYPE_CHOICES),
        label=get_label(Blossom, "petal_connation_type"),
    )
    stamen_num = NumberRangeCharField_to_be_replaced(
        max=11, infinity=True, label=get_label(Blossom, "stamen_num")
    )
    stamen_len = NumberRangeCharField_to_be_replaced(
        0.1, 100, "cm", label=get_label(Blossom, "stamen_len")
    )
    carpel_num = NumberRangeCharField_to_be_replaced(
        max=11, infinity=True, label=get_label(Blossom, "carpel_num")
    )
    stigma_num = NumberRangeCharField_to_be_replaced(
        max=11, infinity=True, label=get_label(Blossom, "stigma_num")
    )

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
    seed_num = NumberRangeCharField_to_be_replaced(
        max=100, infinity=True, label=get_label(Fruit, "seed_num")
    )


class StemRootAdminForm(forms.ModelForm):
    orientation = ArrayMultipleChoiceField(
        ORIENTATION_CHOICES, label=get_label(StemRoot, "orientation")
    )
    appearance = ArrayMultipleChoiceField(
        APPEARANCE_CHOICES,
        label=get_label(StemRoot, "appearance"),
        widget=forms.CheckboxSelectMultiple,
    )
    cross_section = ArrayMultipleChoiceField(
        SR_CROSS_SECTION_CHOICES, label=get_label(StemRoot, "cross_section")
    )
    surface = ArrayMultipleChoiceField(
        SURFACE_CHOICES, label=get_label(StemRoot, "surface")
    )


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
