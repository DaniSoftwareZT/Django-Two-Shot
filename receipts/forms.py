from django import forms
from .models import Receipt


class CreateViewForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "date", "category", "account"]
