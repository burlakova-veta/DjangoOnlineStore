from django.test import TestCase
from .forms import OrderCreateForm


class OrderCreateFormTest(TestCase):

    def test_valid_form(self):
        form = OrderCreateForm(data={
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'email': 'ivanov@example.com',
            'address': 'ул. Ленина, д. 10',
            'postal_code': '123456',
            'city': 'Москва'
        })
        self.assertTrue(form.is_valid(), 'Форма валидна')

    def test_form_invalid(self):
        form = OrderCreateForm(data={
            'first_name': '123456789012345678901234567890123456789012345678901234567890',
            'last_name': '123456789012345678901234567890123456789012345678901234567890',
            'email': 'example',
            'address': '123456789012345678901234567890123456789012345678901234567890',
            'postal_code': '12',
            'city': '123456789012345678901234567890123456789012345678901234567890'
        })
        self.assertFalse(form.is_valid(), 'Форма не валидна')
        self.assertIn('first_name', form.errors.keys(), 'Поле "Имя" не валидно')
        self.assertIn('last_name', form.errors.keys(), 'Поле "Фамилия" не валидно')
        self.assertIn('email', form.errors.keys(), 'Поле "E-mail" не валидно')
        self.assertIn('address', form.errors.keys(), 'Поле "Адрес" не валидно')
        self.assertIn('postal_code', form.errors.keys(), 'Почтовый индекс "фамилия" не валидно')
        self.assertIn('city', form.errors.keys(), 'Поле "Город" не валидно')
