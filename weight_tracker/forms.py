from django import forms

from .models import  Weight

class AddWeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ('title', 'text',)
