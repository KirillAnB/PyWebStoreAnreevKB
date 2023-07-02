from django.urls import path
from .views import CartView, ShopView, ProductSingleView

app_name = 'store'

urlpatterns = [
    path('shop/', ShopView.as_view(), name = 'shop'),
    path('cart/', CartView.as_view(), name = 'cart'),
    path('product/<int:id>/', ProductSingleView.as_view(), name = 'product'),
]