from .models import Product
from django.forms import ModelForm, TextInput, Textarea


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'title', 'full_text', 'price']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Описание"
            })
        }
