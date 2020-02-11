from django.contrib import admin
from .models import GlossaryEntry
from django import forms

# Register your models here.


class HasImgAltForm(forms.ModelForm):
    def clean(self):
        img = self.cleaned_data.get("img")
        img_alt = self.cleaned_data.get("img_alt")
        if img and not img_alt:
            raise forms.ValidationError(
                "An alternative image description needs to be provided."
            )
        super(HasImgAltForm, self).clean()


class GlossaryEntryAdmin(admin.ModelAdmin):
    form = HasImgAltForm
    list_display = ("id", "term")


admin.site.register(GlossaryEntry, GlossaryEntryAdmin)
