from django.db import models
from apps.product import choices
# Create your models here.

class Product(models.Model):
    sku = models.AutoField(
        primary_key = True
    )

    date_registered = models.DateField(
        auto_now_add = True
    )

    product_name = models.CharField(
        max_length = 30
    )

    profile_picture = models.ImageField(
        upload_to = 'static/apps/product/img/profile_pictures',
        null = True
    )
    
    product_brand = models.CharField(
        max_length = 30
    )

    product_Color = models.CharField(
        max_length = 1,
        choices = choices.Colors
    )

    product_size = models.CharField(
        max_length = 30
    )

    product_dimension = models.CharField(
        max_length = 30
    )

    product_price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        null = True,
        default = 0
    )

    num_items = models.PositiveIntegerField(
        default = 0
    )

    def __str__(self):
        return self.product_name

  

