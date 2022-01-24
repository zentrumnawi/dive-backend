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
    BlossomOutput,
    BlossomPoalesOutput,
    FruitOutput,
    InterestingFactsOutput,
    LeafPoalesOutput,
    PlantOutput,
    StemRootOutput,
    StemRhizomePoalesOutput,
)
from .widgets import TrivialNamesWidget


HELP_TEXT = _("Anfängliches Satzzeichen setzen.")
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
    compound_leaf_shape = ArrayMultipleChoiceField(
        COMPOUND_LEAF_SHAPE_CHOICES, label=get_label(Leaf, "compound_leaf_shape")
    )
    compound_leaf_incision_depth = ArrayMultipleChoiceField(
        COMPOUND_LEAF_INCISION_DEPTH_CHOICES,
        label=get_label(Leaf, "compound_leaf_incision_depth"),
    )
    leaflet_incision_depth = ArrayMultipleChoiceField(
        LEAFLET_INCISION_DEPTH_CHOICES, label=get_label(Leaf, "leaflet_incision_depth")
    )
    simple_leaf_shape = ArrayMultipleChoiceField(
        SIMPLE_LEAF_SHAPE_CHOICES, label=get_label(Leaf, "simple_leaf_shape")
    )
    simple_leaf_incision_depth = ArrayMultipleChoiceField(
        SIMPLE_LEAF_INCISION_DEPTH_CHOICES,
        label=get_label(Leaf, "simple_leaf_incision_depth"),
    )
    edge = ArrayMultipleChoiceField(EDGE_CHOICES, label=get_label(Leaf, "edge"))
    surface = ArrayMultipleChoiceField(
        SURFACE_CHOICES, label=get_label(Leaf, "surface")
    )

    compound_leaf_number = IntegerRangeCharField(
        1, 99, label=get_label(Leaf, "compound_leaf_number")
    )
    compound_leaf_incision_number = IntegerRangeCharField(
        1, 99, label=get_label(Leaf, "compound_leaf_incision_number")
    )
    leaflet_incision_number = IntegerRangeCharField(
        1, 99, label=get_label(Leaf, "leaflet_incision_number")
    )
    simple_leaf_number = IntegerRangeCharField(
        1, 99, label=get_label(Leaf, "simple_leaf_number")
    )
    simple_leaf_incision_number = IntegerRangeCharField(
        1, 99, label=get_label(Leaf, "simple_leaf_incision_number")
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
    subsection_title_season = SubsectionTitleField("Blütezeit")
    subsection_title_inflorescence = SubsectionTitleField("Blütenstand")
    subsection_title_general = SubsectionTitleField("Allgemeines")
    subsection_title_diameter = SubsectionTitleField("Durchmesser")
    subsection_title_sepal = SubsectionTitleField("Kelchblatt")
    subsection_title_petal = SubsectionTitleField("Kronblatt")
    subsection_title_tepal = SubsectionTitleField("Perigonblatt")
    subsection_title_stamen = SubsectionTitleField("Staubblatt")
    subsection_title_carpel = SubsectionTitleField("Fruchtblatt")
    subsection_title_specifications = SubsectionTitleField("Spezifikationen")

    season = SeasonField()
    inflorescence_number = IntegerRangeCharField(1, 100, {100: "∞"})
    inflorescence_blossom_number = IntegerRangeCharField(1, 100, {100: "∞"})

    diameter = FloatRangeTermCharField(0, 100, "cm")
    sepal_number = IntegerRangeCharField(1, 11, {11: "∞"})
    sepal_connation_type = NumericPrefixTermField(
        (CONNATION_NUMBER_CHOICES, CONNATION_TYPE_CHOICES),
        label=get_label(Blossom, "sepal_connation_type"),
    )
    petal_number = IntegerRangeCharField(1, 11, {11: "∞"})
    petal_length = FloatRangeTermCharField(0, 100, "cm")
    petal_connation_type = NumericPrefixTermField(
        (CONNATION_NUMBER_CHOICES, CONNATION_TYPE_CHOICES),
        label=get_label(Blossom, "petal_connation_type"),
    )
    tepal_number = IntegerRangeCharField(1, 11, {11: "∞"})
    tepal_connation_type = NumericPrefixTermField(
        (CONNATION_NUMBER_CHOICES, CONNATION_TYPE_CHOICES),
        label=get_label(Blossom, "tepal_connation_type"),
    )
    stamen_number = IntegerRangeCharField(1, 11, {11: "∞"})
    stamen_length = FloatRangeTermCharField(0, 100, "cm")
    carpel_number = IntegerRangeCharField(1, 11, {11: "∞"})
    ovary_number = IntegerRangeCharField(1, 11, {11: "∞"})
    pistil_number = IntegerRangeCharField(1, 11, {11: "∞"})
    stigma_number = IntegerRangeCharField(1, 11, {11: "∞"})

    output_season = OutputField()
    output_inflorescence = OutputField()
    output_general = OutputField()
    output_diameter = OutputField()
    output_sepal = OutputField()
    output_petal = OutputField()
    output_tepal = OutputField()
    output_stamen = OutputField()
    output_carpel = OutputField()

    class Meta:
        model = Blossom
        fields = []
        field_classes = {
            "bract_shape": AdaptedSimpleArrayField,
        }
        widgets = {
            "bract_shape": forms.SelectMultiple(choices=BRACT_SHAPE_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        obj = self.instance

        self.fields["season"].label = obj._meta.get_field("season").verbose_name
        self.fields["inflorescence_number"].label = get_label(
            obj, "inflorescence_number"
        )
        self.fields["inflorescence_blossom_number"].label = get_label(
            obj, "inflorescence_blossom_number"
        )
        self.fields["blossom_sex_distribution_addition"].strip = False
        self.fields["blossom_sex_distribution_addition"].help_text = HELP_TEXT
        self.fields["diameter"].label = get_label(obj, "diameter")
        self.fields["sepal_number"].label = get_label(obj, "sepal_number")
        self.fields["petal_number"].label = get_label(obj, "petal_number")
        self.fields["petal_length"].label = get_label(obj, "petal_length")
        self.fields["tepal_number"].label = get_label(obj, "tepal_number")
        self.fields["stamen_number"].label = get_label(obj, "stamen_number")
        self.fields["stamen_length"].label = get_label(obj, "stamen_length")
        self.fields["stamen_connation_type_addition"].strip = False
        self.fields["stamen_connation_type_addition"].help_text = HELP_TEXT
        self.fields["carpel_number"].label = get_label(obj, "carpel_number")
        self.fields["ovary_number"].label = get_label(obj, "ovary_number")
        self.fields["pistil_number"].label = get_label(obj, "pistil_number")
        self.fields["stigma_number"].label = get_label(obj, "stigma_number")
        self.fields["specifications"].widget.attrs.update(TEXTAREA_ATTRS_80_7)

        self.initial.update(
            {
                "output_season": BlossomOutput.generate_season(obj),
                "output_inflorescence": BlossomOutput.generate_inflorescence(obj),
                "output_general": BlossomOutput.generate_general(obj),
                "output_diameter": BlossomOutput.generate_diameter(obj),
                "output_sepal": BlossomOutput.generate_sepal(obj),
                "output_petal": BlossomOutput.generate_petal(obj),
                "output_tepal": BlossomOutput.generate_tepal(obj),
                "output_stamen": BlossomOutput.generate_stamen(obj),
                "output_carpel": BlossomOutput.generate_carpel(obj),
            }
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
    subsection_title_fruit = SubsectionTitleField("Frucht")
    subsection_title_ovule = SubsectionTitleField("Samenanlage")
    subsection_title_seed = SubsectionTitleField("Samen")

    seed_number = IntegerRangeCharField(1, 100, {100: "∞"})

    output_fruit = OutputField()
    output_ovule = OutputField()
    output_seed = OutputField()

    class Meta:
        model = Fruit
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        obj = self.instance

        self.fields["seed_number"].label = get_label(obj, "seed_number")
        self.fields["winging"].strip = False
        self.fields["winging"].help_text = HELP_TEXT

        self.initial.update(
            {
                "output_fruit": FruitOutput.generate_fruit(obj),
                "output_ovule": FruitOutput.generate_ovule(obj),
                "output_seed": FruitOutput.generate_seed(obj),
            }
        )


class StemRootAdminForm(forms.ModelForm):
    subsection_title_trunk_morphology = SubsectionTitleField("Stammmorphologie")
    subsection_title_stem_morphology = SubsectionTitleField("Sprossmorphologie")
    subsection_title_outgrowths = SubsectionTitleField("Auswüchse")
    subsection_title_milky_sap = SubsectionTitleField("Milchsaft")
    subsection_title_root_morphology = SubsectionTitleField("Wurzelmorphologie")

    output_stem_morphology = OutputField()
    output_outgrowths = OutputField()
    output_root_morphology = OutputField()

    class Meta:
        model = StemRoot
        fields = []
        field_classes = {
            "stem_growth_orientation": AdaptedSimpleArrayField,
            "stem_appearance": AdaptedSimpleArrayField,
            "stem_cross_section": AdaptedSimpleArrayField,
            "stem_surface": AdaptedSimpleArrayField,
        }
        widgets = {
            "stem_growth_orientation": forms.SelectMultiple(
                choices=STEM_GROWTH_ORIENTATION_CHOICES
            ),
            "stem_appearance": forms.CheckboxSelectMultiple(
                choices=STEM_APPEARANCE_CHOICES
            ),
            "stem_cross_section": forms.SelectMultiple(
                choices=SR_STEM_CROSS_SECTION_CHOICES
            ),
            "stem_surface": forms.SelectMultiple(choices=SR_STEM_SURFACE_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        obj = self.instance

        self.fields["trunk_features"].widget.attrs.update(TEXTAREA_ATTRS_60_4)
        self.fields["milky_sap"].widget.attrs.update(TEXTINPUT_ATTRS_60)

        self.initial.update(
            {
                "output_stem_morphology": StemRootOutput.generate_stem_morphology(obj),
                "output_outgrowths": StemRootOutput.generate_outgrowths(obj),
                "output_root_morphology": StemRootOutput.generate_root_morphology(obj),
            }
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
