from dataclasses import field
from django import forms
from .models import Apply

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'
        # exclude = ('job',)