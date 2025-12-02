
from django.db import models
from django.conf import settings

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=2, decimal_places=6)
    updated = models.DateTimeField(auto_now=True)
    inventory = models.PositiveIntegerField()

class Collection(models.Model):
    title = models.CharField(max_length=100)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='collections')

class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    ORDER_STATUS = (
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    placed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default='P')
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=2, decimal_places=6)


