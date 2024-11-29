from django.db import models
from django.urls import reverse


class Product(models.Model):
    image = models.ImageField(upload_to='media/img', null=True, blank=True)
    title = models.CharField('Наименование', max_length=50)
    full_text = models.TextField('Описание', max_length=50)
    price = models.DecimalField('Стоимость', decimal_places=2, max_digits=10, default=0)

    def __str__ (self):
        return self.title

    def get_url(self):
        return reverse('products:product_detail', args=[self.id])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
