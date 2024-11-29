from django.test import TestCase
from .forms import CartAddProductForm


class CartAddProductFormTest(TestCase):

    def test_valid_form(self):
        form = CartAddProductForm(data={
            'quantity': 5,
            'override': False
        })
        self.assertTrue(form.is_valid(), 'Форма валидна')

    def test_invalid_form(self):
        form = CartAddProductForm(data={
            'quantity': 20
        })
        self.assertFalse(form.is_valid(), 'Форма не валидна')
        self.assertIn('quantity', form.errors.keys(), 'Поле "Количество" не валидно')
