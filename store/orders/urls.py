from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'orders'

router = DefaultRouter()
router.register(r'', views.OrderViewSet, basename='order')
router.register(r'<int:pk>', views.OrderItemViewSet, basename='order_item')

urlpatterns = [
    path('api/', include(router.urls)),
    path('create/', views.order_create, name='order_create'),
]
