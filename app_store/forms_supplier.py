# membuat form
from django import forms

from .models import Supplier as ModelSupplier

class FormSupplier(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = ModelSupplier
        fields = ('name',)
        labels = {'name': 'Nama'}
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Erigo',
              #       'value': '',
                    'required': 'required',
                }
            )
        }
