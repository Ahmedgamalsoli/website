from rest_framework import serializers
from .models import Cart, CartItem
from django.contrib.auth.models import User

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

    def create(self, validated_data):
        user = self.context['request'].user
        cart, created = Cart.objects.get_or_create(user=user, checked_out=False)
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity},
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return cart_item