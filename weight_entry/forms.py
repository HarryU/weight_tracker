from django import forms

from .models import Weight

class WeightEntryForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ('name', 'weight', 'date',)

class UserForm(forms.Form):
    queryset = Weight.objects.order_by().values_list('name').distinct()
    users = forms.ModelChoiceField(queryset=queryset, required=True, initial=queryset[0])
