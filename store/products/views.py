from django.shortcuts import render, get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from cart.forms import CartAddProductForm
from rest_framework.viewsets import ModelViewSet


# Класс для работы с API
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer


# Представление для рендера HTML-шаблона
def shop(request):
    product = Product.objects.all().order_by('-id')
    data = {'title': 'Магазин',
            'product': product}
    return render(request, 'products/shop.html', data)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/details.html', {'product': product, 'cart_product_form': cart_product_form})
