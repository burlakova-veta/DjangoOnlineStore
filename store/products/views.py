from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.forms import CartAddProductForm


def shop(request):
    product = Product.objects.order_by('-id')[:15]
    data = {'title': 'Магазин',
            'product': product}
    return render(request, 'products/shop.html', data)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/details.html', {'product': product, 'cart_product_form': cart_product_form})
