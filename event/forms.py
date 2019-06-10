from django.forms import Form, ModelForm, CheckboxSelectMultiple
from . import models


class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
        # exclude = []
        widgets = {
            'event': CheckboxSelectMultiple,
        }
