from django import forms 
from .models import  Questions, Choice


class ChoiceForm(forms.Form):
    choice_option = forms.ModelChoiceField(queryset=Choice.objects.all(), label='Select the answer choice')
