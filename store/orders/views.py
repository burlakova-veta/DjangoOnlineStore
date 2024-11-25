from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from .forms import OrderCreateForm
from .serializers import OrderSerializer, OrderItemSerializer
from cart.cart import Cart
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request,
                          'order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'order/create.html',
                  {'cart': cart, 'form': form})


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer

    def retrieve(self, request, pk=None):
        queryset = OrderItem.objects.all()
        order_item = get_object_or_404(queryset, pk=pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)
