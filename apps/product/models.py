from django.db import models
from apps.product import choices
# Create your models here.


class Product(models.Model):
    sku = models.AutoField(
        primary_key=True
    )

    date_registered = models.DateField(
        auto_now_add=True
    )

    product_category = models.CharField(
        max_length=30
    )

    product_name = models.CharField(
        max_length=30
    )

    profile_picture = models.ImageField(
        upload_to='static/apps/product/img/profile_pictures',
        null=True
    )

    product_brand = models.CharField(
        max_length=30
    )

    color = models.CharField(
        max_length=1,
        choices=choices.Colors
    )

    product_dimension = models.CharField(
        max_length=30
    )

    product_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        default=0
    )

    num_items = models.PositiveIntegerField(
        default=0
    )

    def color_name(self):
        return self.get_color_display() #pylint: disable=no-member

    def full_description(self):
        return "".join(
            [
                str(self.get_color_display()), #pylint: disable=no-member
                " ",
                str(self.product_name),
                " ",
                str(self.product_dimension)
    
            ]
        )


    def __str__(self):
        return self.full_description()

