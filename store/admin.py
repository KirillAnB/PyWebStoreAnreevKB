from django.contrib import admin
from .models import Product, Category, Discount, Cart

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Cart)
