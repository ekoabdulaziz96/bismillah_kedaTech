# membuat form
from django import forms

from .models import Material as ModelMaterial

class FormMaterial(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = ModelMaterial
        fields = (
            'supplier',
            'code',
            'name',
            'type',
            'buyPrice',
        )
        labels = {
            'code': 'Kode',
            'name' : 'Nama',
            'type' : 'Tipe',
            'buyPrice' : 'Harga Beli',
        }
        widgets = {
            'supplier': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'qwe123',
                    'required': 'required',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Kaos Oblong',
                    'required': 'required',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'buyPrice': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    'min': 0,
                    'value': 0,
                    # 'max': 100,
                }
            ),
        }
