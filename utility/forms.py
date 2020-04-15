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
                "Please select an image for upload or leave the \"img alt\" field empty."
        )
        
        super(HasImgForm, self).clean()
