from django import forms


class HasImgAltForm(forms.ModelForm):
    def clean(self):
        img = self.cleaned_data.get("img")
        img_alt = self.cleaned_data.get("img_alt")
        if img and not img_alt:
            raise forms.ValidationError(
                "An alternate text for the image needs to be provided."
            )
        super(HasImgAltForm, self).clean()
