from django.urls import path
from .views import CartView, ShopView, ProductSingleView

urlpatterns = [
    path('shop/', ShopView.as_view()),
    path('cart/', CartView.as_view()),
    path('product/', ProductSingleView.as_view()),
]