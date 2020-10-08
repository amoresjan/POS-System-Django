from django.db import models
from apps.customer.models import Customer
from apps.product.models import Product

# Create your models here.

class Order(models.Model):
    # Date fields
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    # Relations to other models
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Fields for transaction
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    cash_received = models.DecimalField(max_digits=9, decimal_places=2)
    change = models.DecimalField(max_digits=9, decimal_places=2, blank=True)

    def __str__(self):
        return f'Order no.{self.id} by {self.customer.first_name} {self.customer.last_name}'

    def save(self, *args, **kwargs):
        self.final_price = self.product.product_price * self.quantity
        self.change = self.cash_received - self.final_price 
        self.product.num_items = self.product.num_items - self.quantity

        self.product.save()
        super().save(*args, **kwargs)