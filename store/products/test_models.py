from django.test import TestCase
from .models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(title='Наименование продукта',
                               full_text='Описание продукта',
                               price=100.00)

    def test_title_max_length(self):
        product = Product.objects.get(id=1)
        max_len = product._meta.get_field('title').max_length
        self.assertEqual(max_len, 50)

    def test_full_text_max_length(self):
        product = Product.objects.get(id=1)
        max_len = product._meta.get_field('full_text').max_length
        self.assertEqual(max_len, 50)

    def test_price_decimal(self):
        product = Product.objects.get(id=1)
        decimal = product._meta.get_field('price').decimal_places
        self.assertEqual(decimal, 2)

    def test_price_max_digits(self):
        product = Product.objects.get(id=1)
        digits = product._meta.get_field('price').max_digits
        self.assertEqual(digits, 10)

    def test_price_default(self):
        product = Product.objects.get(id=1)
        default = product._meta.get_field('price').default
        self.assertEqual(default, 0)
