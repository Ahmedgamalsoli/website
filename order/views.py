import json
import stripe
from urllib.parse import parse_qs
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect

from cart.cart import Cart

from .models import Order, OrderItem

def start_order(request):
    cart = Cart(request)
    parsed_data = parse_qs(request.body.decode())
    data = json.dumps(parsed_data)
    total_price = 0

    items = []

    for item in cart:
        product = item['product']
        total_price += product.price * int(item['quantity'])

        obj = {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price),
            },
            'quantity': item['quantity']
        }

        items.append(obj)
    
    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url='http://127.0.0.1:8000/cart/success/',
        cancel_url='http://127.0.0.1:8000/cart/'
    )
    payment_intent = session.payment_intent

    first_name = data[1]
    last_name = data[2]
    email = data[3]
    address = data[4]
    zipcode = data[5]
    place = data[6]
    phone = data[7]

    order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, zipcode=zipcode, place=place)
    order.payment_intent = payment_intent
    order.paid_amount = total_price
    order.paid = True
    order.save()

    for item in cart:
        product = item['product']
        quantity = int(item['quantity'])
        price = product.price * quantity

        item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

    return render(request, 'cart/Success.html')
