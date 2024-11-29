from django.core.validators import RegexValidator
from django.test import TestCase
from .models import Order, OrderItem
from products.models import Product


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Order.objects.create(first_name='Иван',
                             last_name='Иванов',
                             email='ivanov@example.com',
                             address='ул. Ленина, д. 10',
                             postal_code='123456',
                             city='Москва')

    def test_first_name_length(self):
        order = Order.objects.get(id=1)
        max_len = order._meta.get_field('first_name').max_length
        self.assertEqual(max_len, 50)

    def test_last_name_length(self):
        order = Order.objects.get(id=1)
        max_len = order._meta.get_field('last_name').max_length
        self.assertEqual(max_len, 50)

    def test_address_length(self):
        order = Order.objects.get(id=1)
        max_len = order._meta.get_field('address').max_length
        self.assertEqual(max_len, 50)

    def test_postal_code_regex_validator(self):
        order = Order.objects.get(id=1)
        regex_validator = order._meta.get_field('postal_code').validators[0]
        self.assertIsInstance(regex_validator, RegexValidator)
        self.assertEqual(regex_validator.regex.pattern, r'^\d{6}$')

    def test_city_length(self):
        order = Order.objects.get(id=1)
        max_len = order._meta.get_field('city').max_length
        self.assertEqual(max_len, 50)

    def test_created_auto_now_add(self):
        order = Order.objects.get(id=1)
        now_add = order._meta.get_field('created').auto_now_add
        self.assertTrue(now_add)

    def test_updated_auto_now(self):
        order = Order.objects.get(id=1)
        now = order._meta.get_field('updated').auto_now
        self.assertTrue(now)

    def test_paid_default_false(self):
        order = Order.objects.get(id=1)
        default = order._meta.get_field('paid').default
        self.assertFalse(default)

    def test_get_total_cost_method(self):
        order = Order.objects.get(id=1)
        total = order.get_total_cost()
        self.assertEqual(total, 0)


class OrderItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        product = Product.objects.create(title='Тестовый продукт',
                                         price=100)
        order = Order.objects.create(first_name='Иван',
                                     last_name='Иванов',
                                     email='ivanov@example.com',
                                     address='ул. Ленина, д. 10',
                                     postal_code='123456',
                                     city='Москва')
        OrderItem.objects.create(order=order,
                                 product=product,
                                 price=100,
                                 quantity=2)

    def test_order_relationship(self):
        order_item = OrderItem.objects.get(id=1)
        self.assertIsInstance(order_item.order, Order)

    def test_product_relationship(self):
        order_item = OrderItem.objects.get(id=1)
        self.assertIsInstance(order_item.product, Product)

    def test_price_decimal(self):
        order_item = OrderItem.objects.get(id=1)
        self.assertEqual(order_item.price, 100.00)

    def test_quantity_pos_integer(self):
        order_item = OrderItem.objects.get(id=1)
        self.assertGreaterEqual(order_item.quantity, 1)
