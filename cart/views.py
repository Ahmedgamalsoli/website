from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

from .cart import Cart

from item.models import Item

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')

def cart(request):
    return render(request, 'cart/cart.html')

def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)
    
    product = Item.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)['quantity']

    item = {
        'product': {
            'id': product.id,
            'name': product.name,
            'image': product.image,
            'price': product.price,
        },
        'total_price': (quantity * product.price),
        'quantity': quantity,
    }

    response = render(request, 'cart/partials/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response

@login_required
def checkout(request):
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE 
    return render(request, 'cart/checkout.html', {'pub_key': pub_key})

def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')

def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')