from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('event', 'name', 'tell', 'age')
        # exclude = []
        widgets = {
            'event': forms.CheckboxSelectMultiple,
        }
