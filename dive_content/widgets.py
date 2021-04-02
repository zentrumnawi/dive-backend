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
