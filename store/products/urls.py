from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'products'

router = DefaultRouter()
router.register(r'', views.ProductViewSet, basename='product_list')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.shop, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail')
]
