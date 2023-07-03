from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import OuterRef,F, ExpressionWrapper, DecimalField, Case, When
from django.utils import timezone
from .models import Discount, Product

# Создание запроса на получения всех действующих скидок


# Create your views here.
class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')

class ProductSingleView(View):
    def get(self, request, id):
        data = Product.objects.get(id=id)
        return render(request, "store/product-single.html", context={'name': data.name,
                               'description': data.description,
                               'price': data.price,
                               'rating': 5.0,
                               'url': data.image.url,
                               })
    # def get(self, request, id):
    #     data = {1: {'name': 'Bell Pepper',
    #                 'description': 'Bell Pepper',
    #                 'price': 120.00,
    #                 'rating': 5.0,
    #                 'url': 'store/images/product-1.jpg'},
    #             2: {'name': 'Strawberry',
    #                 'description': 'Strawberry',
    #                 'price': 120.00,
    #                 'rating': 5.0,
    #                 'url': 'store/images/product-2.jpg'},
    #             3: {'name': 'Green Beans',
    #                 'description': 'Green Beans',
    #                 'price': 120.00,
    #                 'rating': 5.0,
    #                 'url': 'store/images/product-3.jpg'},
    #             4: {'name': 'Purple Cabbage',
    #                 'description': 'Purple Cabbage',
    #                 'price': 120.00,
    #                 'rating': 5.0,
    #                 'url': 'store/images/product-4.jpg'},
    #             5: {'name': 'Tomatoe',
    #                 'description': 'Tomatoe',
    #                 'price': 120.00,
    #                 'rating': 5.0,
    #                 'url': 'store/images/product-5.jpg'},
    #             6: {'name': 'Brocolli',
    #                 'description': 'Brocolli',
    #                 'price': 120.00,
    #                 'rating': 5.0,
    #                 'url': 'store/images/product-6.jpg'},
    #             7: {'name': 'Carrots',
    #                 'description': 'Carrots',
    #                 'price': 120.00,
    #                 'rating': 5.0,
    #                 'url': 'store/images/product-7.jpg'},
    #             8: {'name': 'Fruit Juice',
    #                 'description': 'Fruit Juice',
    #                 'price': 120.00,
    #                 'rating': 5.0,
    #                 'url': 'store/images/product-8.jpg'},
    #             9: {'name': 'Onion',
    #                 'description': 'Onion',
    #                 'price': 120.00,
    #                 'rating': 5.0,
    #                 'url': 'store/images/product-9.jpg'},
    #             10: {'name': 'Apple',
    #                  'description': 'Apple',
    #                  'price': 120.00,
    #                  'rating': 5.0,
    #                  'url': 'store/images/product-10.jpg'},
    #             11: {'name': 'Garlic',
    #                  'description': 'Garlic',
    #                  'price': 120.00,
    #                  'rating': 5.0,
    #                  'url': 'store/images/product-11.jpg'},
    #             12: {'name': 'Chilli',
    #                  'description': 'Chilli',
    #                  'price': 120.00,
    #                  'rating': 5.0,
    #                  'url': 'store/images/product-12.jpg'}
    #             }
    #
    #     return render(request, 'store/product-single.html', context=data[id])

class ShopView(View):
    def get(self, request):
        # context = {'data': [{'name': 'Bell Pepper',
        #                      'id':1,
        #                      'discount': 30,
        #                      'price_before': 120.00,
        #                      'price_after': 80.00,
        #                      'url': 'store/images/product-1.jpg'},
        #                     {'name': 'Strawberry',
        #                      'id':2,
        #                      'discount': None,
        #                      'price_before': 120.00,
        #                      'url': 'store/images/product-2.jpg'},
        #                     {'name': 'Green Beans',
        #                      'id': 3,
        #                      'discount': None,
        #                      'price_before': 120.00,
        #                      'url': 'store/images/product-3.jpg'},
        #                     {'name': 'Purple Cabbage',
        #                      'id': 4,
        #                      'discount': None,
        #                      'price_before': 120.00,
        #                      'url': 'store/images/product-4.jpg'},
        #                     {'name': 'Tomatoe',
        #                      'id': 5,
        #                      'discount': 30,
        #                      'price_before': 120.00,
        #                      'price_after': 80.00,
        #                      'url': 'store/images/product-5.jpg'},
        #                     {'name': 'Brocolli',
        #                      'id': 6,
        #                      'discount': None,
        #                      'price_before': 120.00,
        #                      'url': 'store/images/product-6.jpg'},
        #                     {'name': 'Carrots',
        #                      'id': 7,
        #                      'discount': None,
        #                      'price_before': 120.00,
        #                      'url': 'store/images/product-7.jpg'},
        #                     {'name': 'Fruit Juice',
        #                      'id': 8,
        #                      'discount': None,
        #                      'price_before': 120.00,
        #                      'url': 'store/images/product-8.jpg'},
        #                     {'name': 'Onion',
        #                      'id': 9,
        #                      'discount': 30,
        #                      'price_before': 120.00,
        #                      'price_after': 80.00,
        #                      'url': 'store/images/product-9.jpg'},
        #                     {'name': 'Apple',
        #                      'id': 10,
        #                      'discount': None,
        #                      'price_before': 120.00,
        #                      'url': 'store/images/product-10.jpg'},
        #                     {'name': 'Garlic',
        #                      'id': 11,
        #                      'discount': None,
        #                      'price_before': 120.00,
        #                      'url': 'store/images/product-11.jpg'},
        #                     {'name': 'Chilli',
        #                      'id': 12,
        #                      'discount': None,
        #                      'price_before': 120.00,
        #                      'url': 'store/images/product-12.jpg'},
        #                     ]
        #            }
        discount_value = Case(When(discount__value__gte=0,
                                   discount__date_begin__lte=timezone.now(),
                                   discount__date_end__gte=timezone.now(),
                                   then=F('discount__value')),
                              default=0,
                              output_field=DecimalField(max_digits=10, decimal_places=2)
                              )

        price_with_discount = ExpressionWrapper(
            F('price') * (100.0 - F('discount_value')) / 100.0,
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )

        products = Product.objects.annotate(
            discount_value=discount_value,
            price_before=F('price'),
            price_after=price_with_discount
        ).values('id', 'name', 'image', 'price_before', 'price_after',
                 'discount_value')
        return render(request, 'store/shop.html', {'data': products})

