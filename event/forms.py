from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
        # exclude = []
        widgets = {
            #'event': forms.CheckboxSelectMultiple,
        }
