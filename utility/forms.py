from django import forms


class HasImgForm(forms.ModelForm):
    """
    Validation if an image and an alternate text for the image are provided
    together.
    """

    def clean(self):
        img = self.cleaned_data.get("img")
        img_alt = self.cleaned_data.get("img_alt")

        if img and not img_alt:
            raise forms.ValidationError(
                "An alternate text for the image needs to be provided."
            )

        if img_alt and not img:
            raise forms.ValidationError(
                'Please select an image for upload or leave the "img alt" field empty.'
            )

        super(HasImgForm, self).clean()


class DateOrderForm(forms.ModelForm):
    """
    Validation whether a validity start date and end date are in the correct
    order.
    """

    def clean(self):
        valid_from = self.cleaned_data.get("valid_from")
        valid_to = self.cleaned_data.get("valid_to")

        if valid_to < valid_from:
            raise forms.ValidationError(
                "The validity end date must be equel with or after the start date."
            )

        super(DateOrderForm, self).clean()
