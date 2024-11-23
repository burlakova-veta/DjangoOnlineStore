from django.db import models
from django.urls import reverse


class Product(models.Model):
    image = models.ImageField(upload_to='media/img', null=True, blank=True)
    title = models.CharField('Наименование', max_length=150)
    full_text = models.TextField('Описание')
    price = models.CharField('Стоимость', max_length=7, default='0р')

    def __str__ (self):
        return self.title

    def get_url(self):
        return reverse('products:product_detail', args=[self.id])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
