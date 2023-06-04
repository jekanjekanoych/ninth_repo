from django import forms

from .models import Number
from .models import Code


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ["number"]


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ["number", "code"]
