from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = {}

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity, 'id': product_id}
        elif update_quantity:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id]['quantity'] = quantity

        if self.cart[product_id]['quantity'] <= 0:
            self.remove(product_id)

        self.save()

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

	
class CartItem(models.Model):
	product = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	#date_added = models.DateTimeField(auto_now_add=True)
	cart = models.ForeignKey(Cart,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.quantity} x {self.product.price}'
