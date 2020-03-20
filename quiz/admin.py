from django.contrib import admin
from django import forms
from .models import QuizQuestion, QuizAnswer


class HasImgAltForm(forms.ModelForm):
    def clean(self):
        img = self.cleaned_data.get("img")
        img_alt = self.cleaned_data.get("img_alt")
        if img and not img_alt:
            raise forms.ValidationError(
                "An alternate text for the image needs to be provided."
            )
        super(HasImgAltForm, self).clean()


class QuizQuestionAdmin(admin.ModelAdmin):
    form = HasImgAltForm
    list_display = ("id", "text")


admin.site.register(QuizQuestion, QuizQuestionAdmin)


class QuizAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "text", "correct")


admin.site.register(QuizAnswer, QuizAnswerAdmin)
