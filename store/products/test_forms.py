from django.test import TestCase
from .forms import ProductForm


class ProductFormTest(TestCase):

    # проверка на валидность
    def test_valid_form(self):
        form = ProductForm(data={
            'title': 'Наименование',
            'full_text': 'Описание товара',
            'price': '5000',
        })
        self.assertTrue(form.is_valid(), 'Форма валидна')

    # проверка на невалидность
    def test_invalid_form(self):
        form = ProductForm(data={
            'title': '123456789012345678901234567890123456789012345678901234567890',
            'full_text': '123456789012345678901234567890123456789012345678901234567890',
            'price': '5000рублей',
        })
        self.assertFalse(form.is_valid(), 'Форма не валидна')

        self.assertIn('title', form.errors.keys(), 'Поле "Наименование" не валидно')
        self.assertIn('full_text', form.errors.keys(), 'Поле "Описание" не валидно')
        self.assertIn('price', form.errors.keys(), 'Поле "Цена" не валидна')
