from django import forms


class IndicatorWidget(forms.MultiWidget):
    def __init__(self, choices, mode=None, attrs=None):
        self.mode = mode
        widgets = [
            forms.Select(choices=choices),
            forms.CheckboxInput(),
        ]
        if mode == "light":
            widgets.append(forms.CheckboxInput())
            widgets[1].template_name = "parentheses.html"
        if mode == "humidity":
            widgets.extend([forms.CheckboxInput(), forms.CheckboxInput()])
            widgets[1].template_name = "tilde.html"
            widgets[2].template_name = "equalssign.html"
        widgets[-1].template_name = "questionmark.html"

        super().__init__(widgets, attrs)

    def decompress(self, value):
        data_list = [None] * 2
        if self.mode == "light":
            data_list = [None] * 3
        if self.mode == "humidity":
            data_list = [None] * 4

        if value:
            data_list = [
                value[:2],
                True if "(?)" in value else False,
            ]
            if self.mode == "light":
                data_list.insert(1, True if "()" in value else False)
            if self.mode == "humidity":
                if value[2:3].isdigit():
                    data_list[0] = value[:3]
                data_list.insert(1, True if "~" in value else False)
                data_list.insert(2, True if "=" in value else False)

        return data_list


class NumberRangeCharWidget(forms.MultiWidget):
    def __init__(self, min, max, reversed_substitutes={}, attrs=None):
        self.reversed_substitutes = reversed_substitutes
        widgets = (
            forms.NumberInput(attrs={"min": min, "max": max}),
            forms.NumberInput(attrs={"min": min, "max": max}),
        )

        super().__init__(widgets, attrs)

    def decompress(self, value):
        data_list = [None, None]
        if value:
            data_list = value.split("–", 1)
            if self.reversed_substitutes:
                for i, data in enumerate(data_list):
                    if data in self.reversed_substitutes:
                        data_list[i] = self.reversed_substitutes[data]

        return data_list


class NumberRangeTermCharWidget(forms.MultiWidget):
    template_name = "rangeterm.html"

    def __init__(self, min, max, term, separator, attrs=None):
        self.term = None if isinstance(term, (tuple, list)) else term
        self.separator = separator

        widgets = (NumberRangeCharWidget(min, max),)
        if self.term is None:
            widgets += (forms.Select(choices=term),)

        super().__init__(widgets, attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["term"] = self.term
        context["widget"]["separator"] = self.separator

        return context

    def decompress(self, value):
        if self.term is None:
            data_list = value.split(self.separator, 1) if value else ["", ""]
        else:
            data_list = [value.split(self.separator, 1)[0]] if value else [""]

        return data_list


class NumericPrefixTermWidget(forms.MultiWidget):
    def __init__(self, choices, attrs=None):
        widgets = (
            forms.Select(choices=choices[0]),
            forms.Select(choices=choices[1]),
        )

        super().__init__(widgets, attrs)

    def decompress(self, value):
        data_list = ["", ""]
        if value:
            data_list = [value[0], value[1:]] if value[0].isdigit() else ["", value]

        return data_list


class OutputWidget(forms.Widget):
    def __init__(self):
        self.template_name = "output.html"
        super().__init__()


class SeasonWidget(forms.MultiWidget):
    def __init__(self, choices, attrs=None):
        self.template_name = "season.html"
        widgets = [forms.Select(choices=choices)] * 4

        super().__init__(widgets, attrs)

    def decompress(self, value):
        return [None] * 4


class StemSurfaceWidget(NumberRangeTermCharWidget):
    def decompress(self, value):
        data_list = ["", ""]
        if value:
            data_list = value.split(" ", 1)
            if len(data_list) == 1:
                data_list.insert(0, "")

        return data_list


class TrivialNameWidget(forms.MultiWidget):
    template_name = "multiwidget.html"

    def __init__(self, choices, attrs=None):
        widgets = [
            forms.Select(choices=choices),
            forms.TextInput(
                attrs={"size": 25, "maxlength": 50, "placeholder": "Trivialname"}
            ),
        ]

        super().__init__(widgets, attrs)

    def decompress(self, value):
        return value.split(",") if value else []


class TrivialNamesWidget(forms.MultiWidget):
    template_name = "multiwidget.html"

    def __init__(self, attrs=None):
        widgets = [
            forms.TextInput(
                attrs={
                    "size": 25,
                    "maxlength": 50,
                    "placeholder": "Trivialname",
                    "required": False,
                }
            )
        ] * 4

        super().__init__(widgets, attrs)

    def decompress(self, value):
        return value.split(",") if value else []

    def value_from_datadict(self, data, files, name):
        value = super().value_from_datadict(data, files, name)
        value = list(filter(None, value))

        return value
