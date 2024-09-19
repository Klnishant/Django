from django import forms
from .models import ChaiVariety

class chaiVarietyForms(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(),label='select chai variety')
    