from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length =255)
    price = models.IntegerField()

    imge = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price