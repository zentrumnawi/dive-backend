from django import forms

from .models import Plant

class PlantModelForm(forms.ModelForm):

    habitat = forms.MultipleChoiceField(choices=Plant.HABITAT_CHOICES)
    ground = forms.MultipleChoiceField(choices=Plant.GROUND_CHOICES)

    class Meta:
        model = Plant
        fields = "__all__"
