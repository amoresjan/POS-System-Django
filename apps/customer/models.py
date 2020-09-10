from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=30
    )
    address = models.CharField(
        max_length = 50
    )
    date_registered = models.DateField(
        auto_now_add = True
    )
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name

    
