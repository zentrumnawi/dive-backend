from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .choices import *
from .fields import (
    AdaptedSimpleArrayField,
    ArrayMultipleChoiceField,
    FloatRangeTermCharField,
    IndicatorField,
    IntegerRangeCharField,
    NumberRangeCharField_to_be_replaced,
    NumericPrefixTermField,
    OutputField,
    SeasonField,
    StemSurfaceField,
    SubsectionTitleField,
    TrivialNameField,
)
from .models import (
    Blossom,
    BlossomPoales,
    Fruit,
    InterestingFacts,
    Leaf,
    LeafPoales,
    Plant,
    StemRhizomePoales,
    StemRoot,
)
from .outputs import (
    BlossomPoalesOutput,
    InterestingFactsOutput,
    LeafPoalesOutput,
    PlantOutput,
    StemRhizomePoalesOutput,
)
from .widgets import TrivialNamesWidget


TEXTAREA_ATTRS_60_4 = {"cols": 60, "rows": 4, "class": False}
TEXTAREA_ATTRS_80_7 = {"cols": 80, "rows": 7, "class": False}
TEXTINPUT_ATTRS_60 = {"size": 60, "class": False}
TEXTINPUT_ATTRS_80 = {"size": 80, "class": False}


def get_label(model, field_name):
    label = model._meta.get_field(field_name).verbose_name
    if isinstance(model._meta.get_field(field_name), ArrayField):
        label = model._meta.get_field(field_name).base_field.verbose_name

    return label


class PlantAdminForm(forms.ModelForm):
    subsection_title_general = SubsectionTitleField("Allgemeines")

    article_trivial_name = TrivialNameField()
    growth_height = FloatRangeTermCharField(0, 200, GROWTH_HEIGHT_UNITS)

    output_general = OutputField()

    class Meta:
        model = Plant
        fields = []
        field_classes = {
            "alternative_trivial_names": AdaptedSimpleArrayField,
            "habitats": AdaptedSimpleArrayField,
            "ruderal_sites": AdaptedSimpleArrayField,
        }
        widgets = {
            "alternative_trivial_names": TrivialNamesWidget,
            "habitats": forms.SelectMultiple(choices=HABITATS_CHOICES),
            "ruderal_sites": forms.SelectMultiple(choices=RUDERAL_SITES_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        obj = self.instance

        self.fields["short_description"].widget.attrs.update(TEXTAREA_ATTRS_80_7)
        self.fields["article_trivial_name"].label = get_label(obj, "trivial_name")
        self.fields["growth_height"].label = get_label(obj, "growth_height")
        self.fields["other_features"].widget.attrs.update(TEXTINPUT_ATTRS_80)

        self.initial.update(
            {
                "article_trivial_name": [obj.article, obj.trivial_name],
                "output_general": PlantOutput.generate_general(obj),
            }
        )

    def clean(self):
        super().clean()
        fields = (
            "alternative_trivial_names",
            "growth_form",
            "growth_height",
        )
        cleaned_fields = (self.cleaned_data.get(field) for field in fields)

        if not any(cleaned_fields):
            for field in fields:
                self.add_error(field, "At least one of these fields must be provided")

        fields = (
            "interaction",
            "ground",
            "habitats",
            "ruderal_sites",
        )
        cleaned_fields = (self.cleaned_data.get(field) for field in fields)

        if not self.cleaned_data.get("dispersal_form") and any(cleaned_fields):
            self.add_error(
                "dispersal_form",
                "In combination with others this field must be provided.",
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        initial = [instance.article, instance.trivial_name]
        data = self.cleaned_data["article_trivial_name"]
        if self.fields["article_trivial_name"].has_changed(initial, data):
            instance.article = data[0]
            instance.trivial_name = data[1]

        if commit:
            instance.save()

        return instance


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

    leaf_comp_num = IntegerRangeCharField(1, 99, label=get_label(Leaf, "leaf_comp_num"))
    leaf_comp_incision_num = IntegerRangeCharField(
        1, 99, label=get_label(Leaf, "leaf_comp_incision_num")
    )
    leaflet_incision_num = IntegerRangeCharField(
        1, 99, label=get_label(Leaf, "leaflet_incision_num")
    )
    leaf_simple_num = IntegerRangeCharField(
        1, 99, label=get_label(Leaf, "leaf_simple_num")
    )
    leaf_simple_incision_num = IntegerRangeCharField(
        1, 99, label=get_label(Leaf, "leaf_simple_incision_num")
    )


class LeafPoalesAdminForm(forms.ModelForm):
    subsection_title_overview = SubsectionTitleField("Überblick")
    subsection_title_leaf_blade = SubsectionTitleField("Blattspreite")
    subsection_title_leaf_base = SubsectionTitleField("Blattgrund")
    subsection_title_ligule = SubsectionTitleField("Blatthäutchen")
    subsection_title_leaf_sheath = SubsectionTitleField("Blattscheide")

    length = FloatRangeTermCharField(0, 100, "cm")
    alignment = NumericPrefixTermField((ALIGNMENT_NUM_CHOICES, ALIGNMENT_CHOICES))

    output_overview = OutputField()
    output_leaf_blade = OutputField()
    output_leaf_base = OutputField()
    output_ligule = OutputField()
    output_leaf_sheath = OutputField()

    class Meta:
        model = LeafPoales
        fields = []
        field_classes = {
            "hairiness": AdaptedSimpleArrayField,
            "cross_section": AdaptedSimpleArrayField,
            "blade_corrugation": AdaptedSimpleArrayField,
        }
        widgets = {
            "hairiness": forms.SelectMultiple(choices=HAIRINESS_CHOICES),
            "cross_section": forms.SelectMultiple(
                choices=LEAFPOALES_CROSS_SECTION_CHOICES
            ),
            "blade_corrugation": forms.CheckboxSelectMultiple(
                choices=BLADE_CORRUGATION_CHOICES
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        obj = self.instance

        self.fields["length"].label = get_label(obj, "length")
        self.fields["alignment"].label = get_label(obj, "alignment",)
        self.fields["ligule_features"].widget.attrs.update(TEXTINPUT_ATTRS_60)
        self.fields["sheath_features"].widget.attrs.update(TEXTINPUT_ATTRS_60)

        self.initial.update(
            {
                "output_overview": LeafPoalesOutput.generate_overview(obj),
                "output_leaf_blade": LeafPoalesOutput.generate_leaf_blade(obj),
                "output_leaf_base": LeafPoalesOutput.generate_leaf_base(obj),
                "output_ligule": LeafPoalesOutput.generate_ligule(obj),
                "output_leaf_sheath": LeafPoalesOutput.generate_leaf_sheath(obj),
            }
        )


class BlossomAdminForm(forms.ModelForm):
    season = SeasonField(label=get_label(Blossom, "season"))
    inflorescence_number = IntegerRangeCharField(
        1, 100, {100: "∞"}, label=get_label(Blossom, "inflorescence_number")
    )
    inflorescence_blossom_number = IntegerRangeCharField(
        1, 100, {100: "∞"}, label=get_label(Blossom, "inflorescence_blossom_number")
    )
    bract_shape = ArrayMultipleChoiceField(
        BRACT_SHAPE_CHOICES, label=get_label(Blossom, "bract_shape")
    )
    diameter = NumberRangeCharField_to_be_replaced(
        0.1, 100, "cm", label=get_label(Blossom, "diameter")
    )
    sepal_number = IntegerRangeCharField(
        1, 11, {11: "∞"}, label=get_label(Blossom, "sepal_number")
    )
    sepal_connation_type = NumericPrefixTermField(
        (CONNATION_NUMBER_CHOICES, CONNATION_TYPE_CHOICES),
        label=get_label(Blossom, "sepal_connation_type"),
    )
    petal_number = IntegerRangeCharField(
        1, 11, {11: "∞"}, label=get_label(Blossom, "petal_number")
    )
    petal_length = NumberRangeCharField_to_be_replaced(
        0.1, 100, "cm", label=get_label(Blossom, "petal_length")
    )
    petal_connation_type = NumericPrefixTermField(
        (CONNATION_NUMBER_CHOICES, CONNATION_TYPE_CHOICES),
        label=get_label(Blossom, "petal_connation_type"),
    )
    stamen_number = IntegerRangeCharField(
        1, 11, {11: "∞"}, label=get_label(Blossom, "stamen_number")
    )
    stamen_length = NumberRangeCharField_to_be_replaced(
        0.1, 100, "cm", label=get_label(Blossom, "stamen_length")
    )
    carpel_number = IntegerRangeCharField(
        1, 11, {11: "∞"}, label=get_label(Blossom, "carpel_number")
    )
    stigma_number = IntegerRangeCharField(
        1, 11, {11: "∞"}, label=get_label(Blossom, "stigma_number")
    )

    def clean_bract_shape(self):
        value = self.cleaned_data.get("bract_shape")
        error_messages = {"invalid_choice": _(f"Selected combination not allowed.")}

        if (
            any(v in dict(BRACT_SHAPE_SUBCHOICES[0]).keys() for v in value)
            and any(v in dict(BRACT_SHAPE_SUBCHOICES[1]).keys() for v in value)
        ) or (BRACT_SHAPE_SUBCHOICES[2][0][0] in value and len(value) > 1):
            raise ValidationError(error_messages["invalid_choice"])

        return value

    def save(self, commit=True):
        # Clear inflorescence_blossom_number if option "Einzelblüte" is selected as inflorescence_type.
        instance = super().save(commit=False)

        inflorescence_type = self.cleaned_data.get("inflorescence_type", "")
        inflorescence_blossom_number = self.cleaned_data.get(
            "inflorescence_blossom_number", ""
        )
        if inflorescence_type == "ein" and inflorescence_blossom_number:
            instance.inflorescence_blossom_number = ""

        if commit:
            instance.save()

        return instance


class BlossomPoalesAdminForm(forms.ModelForm):
    subsection_title_season = SubsectionTitleField("Blütezeit")
    subsection_title_inflorescence = SubsectionTitleField("Blütenstand")
    subsection_title_blossom_perianth = SubsectionTitleField("Blüte und Blütenhülle")
    subsection_title_spikelet = SubsectionTitleField("Ährchen")
    subsection_title_husks = SubsectionTitleField("Spelzen")

    season = SeasonField()
    inflorescence_blossom_number = IntegerRangeCharField(1, 12, {11: "viel", 12: "∞"})
    inflorescence_bract_length = FloatRangeTermCharField(0, 99, "cm")
    spikelet_length = FloatRangeTermCharField(0, 99, "cm")
    spikelet_blossom_number = IntegerRangeCharField(2, 11, {11: "∞"})

    output_season = OutputField()
    output_inflorescence = OutputField()
    output_blossom_perianth = OutputField()
    output_spikelet = OutputField()
    output_husks = OutputField()

    class Meta:
        model = BlossomPoales
        fields = []
        field_classes = {
            "husks_cross_section": AdaptedSimpleArrayField,
        }
        widgets = {
            "husks_cross_section": forms.CheckboxSelectMultiple(
                choices=HUSKS_CROSS_SECTION_CHOICES
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        obj = self.instance

        self.fields["season"].label = obj._meta.get_field("season").verbose_name
        self.fields["inflorescence_blossom_number"].label = get_label(
            obj, "inflorescence_blossom_number"
        )
        self.fields["inflorescence_bract_length"].label = get_label(
            obj, "inflorescence_bract_length"
        )
        self.fields["blossom_description"].widget.attrs.update(TEXTAREA_ATTRS_60_4)
        self.fields["perianth_description"].widget.attrs.update(TEXTAREA_ATTRS_60_4)
        self.fields["spikelet_length"].label = get_label(obj, "spikelet_length")
        self.fields["spikelet_blossom_number"].label = get_label(
            obj, "spikelet_blossom_number"
        )
        self.fields["spikelet_features"].widget.attrs.update(TEXTINPUT_ATTRS_60)
        self.fields["husks_description"].widget.attrs.update(TEXTAREA_ATTRS_60_4)

        self.initial.update(
            {
                "output_season": BlossomPoalesOutput.generate_season(obj),
                "output_inflorescence": BlossomPoalesOutput.generate_inflorescence(obj),
                "output_blossom_perianth": BlossomPoalesOutput.generate_blossom_perianth(
                    obj
                ),
                "output_spikelet": BlossomPoalesOutput.generate_spikelet(obj),
                "output_husks": BlossomPoalesOutput.generate_husks(obj),
            }
        )

    def clean(self):
        super().clean()
        fields = (
            "inflorescence_blossom_number",
            "inflorescence_density",
            "inflorescence_position",
            "inflorescence_features",
        )
        cleaned_fields = (self.cleaned_data.get(field) for field in fields)

        if not self.cleaned_data.get("inflorescence_type") and any(cleaned_fields):
            self.add_error(
                "inflorescence_type",
                "In combination with others this field must be provided.",
            )


class FruitAdminForm(forms.ModelForm):
    seed_num = IntegerRangeCharField(
        1, 100, {100: "∞"}, label=get_label(Fruit, "seed_num")
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


class StemRhizomePoalesAdminForm(forms.ModelForm):
    subsection_title_growth_form = SubsectionTitleField("Wuchsform")
    subsection_title_stem = SubsectionTitleField("Stängel")
    subsection_title_rhizome = SubsectionTitleField("Rhizom")

    stem_surface = StemSurfaceField(1, 99, STEM_SURFACE_CHOICES)

    output_growth_form = OutputField()
    output_stem = OutputField()
    output_rhizome = OutputField()

    class Meta:
        model = StemRhizomePoales
        fields = []
        field_classes = {
            "stem_cross_section": AdaptedSimpleArrayField,
        }
        widgets = {
            "stem_cross_section": forms.CheckboxSelectMultiple(
                choices=STEM_CROSS_SECTION_CHOICES
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        obj = self.instance

        self.fields["stem_surface"].label = get_label(obj, "stem_surface")
        self.fields["stem_features"].widget.attrs.update(TEXTINPUT_ATTRS_60)

        self.initial.update(
            {
                "output_growth_form": StemRhizomePoalesOutput.generate_growth_form(obj),
                "output_stem": StemRhizomePoalesOutput.generate_stem(obj),
                "output_rhizome": StemRhizomePoalesOutput.generate_rhizome(obj),
            }
        )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get("stem_pith", "") == "n":
            instance.stem_nodes = "m"
        if instance.stem_nodes != "m":
            instance.stem_nodes_hairiness = ""

        if commit:
            instance.save()

        return instance


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


class InterestingFactsAdminForm(forms.ModelForm):
    output_pollination = OutputField()
    output_dispersal = OutputField()

    class Meta:
        model = InterestingFacts
        fields = []
        field_classes = {
            "pollination": AdaptedSimpleArrayField,
            "dispersal": AdaptedSimpleArrayField,
        }
        widgets = {
            "pollination": forms.CheckboxSelectMultiple(choices=POLLINATION_CHOICES),
            "dispersal": forms.CheckboxSelectMultiple(choices=DISPERSAL_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        obj = self.instance

        self.fields["detail_features"].widget.attrs.update(TEXTINPUT_ATTRS_80)
        self.fields["usage"].widget.attrs.update(TEXTINPUT_ATTRS_80)
        self.fields["trivia"].widget.attrs.update(TEXTAREA_ATTRS_80_7)

        self.initial.update(
            {
                "output_pollination": InterestingFactsOutput.generate_pollination(obj),
                "output_dispersal": InterestingFactsOutput.generate_dispersal(obj),
            }
        )
