from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from .models import Product


class ShopPageTest(StaticLiveServerTestCase):
    fixtures = ['product.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Edge()
        cls.driver.implicitly_wait(10)

    def test(self):
        self.driver.get(f'{self.live_server_url}/products/4/')
        elements = self.driver.find_elements(By.XPATH, '//p[@class="price"]')
        for elem in elements:
            self.assertIn(float(elem.text.replace(',', '.')), list(map(lambda b: float(b.price), Product.objects.all())))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
