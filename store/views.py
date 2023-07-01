from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')

class ProductSingleView(View):
    def get(self, request):
        return render(request, 'store/product-single.html')

class ShopView(View):
    def get(self, request):
        return render(request, 'store/shop.html')
