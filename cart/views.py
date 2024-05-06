from django.shortcuts import render, redirect
from .models import  CartItem ,Cart
from rest_framework import generics
from item.models import Item
from .Serializers import CartItemSerializer
from django.contrib.auth.models import User

class CartItemView (generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    def get_queryset(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return CartItem.objects.filter(cart=cart)


        
    def perform_create(self, serializer):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        serializer.save(cart=cart)
        
        
def checkout(request):
    return render(request, 'cart/checkout.html')

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')