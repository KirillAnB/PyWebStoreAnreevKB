from rest_framework import serializers
from .models import Cart, Wishlist
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class WishListSerrializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'