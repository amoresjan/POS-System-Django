from django.db import models
from apps.customer import choices
from django_countries.fields import CountryField
from stdimage import StdImageField, JPEGField

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(
        max_length = 30
    )
    middle_name = models.CharField(
        max_length = 30,
        blank = True,
        null = True
    )
    last_name = models.CharField(
        max_length = 30
    )
    profile_picture = models.ImageField(
        blank = True,
        upload_to = 'static/apps/customer/img/profile_pictures/'
    )
    

    street = models.CharField(
        max_length = 50,
        default = ''
    )
    barangay = models.CharField(
        max_length = 50,
        default = ''
    )
    city = models.CharField(
        max_length = 50
    )
    province = models.CharField(
        max_length = 50
    )
    zip_code = models.CharField(
        max_length = 4
    )
    country = CountryField()

    gender = models.CharField(
        max_length = 1,
        choices = choices.Gender.choices
    )
    birth_date = models.DateField()
    status = models.CharField(
        max_length = 1,
        choices = choices.Status.choices,
    )

    spouse_name = models.CharField(
        blank = True,
        max_length = 70
    )
    spouse_occupation = models.CharField(
        blank = True,
        max_length = 30
    )
    number_of_children = models.PositiveIntegerField(
        default = 0
    )
    
    mother_name = models.CharField(
        blank = True,
        max_length = 70
    )
    mother_occupation = models.CharField(
        blank = True,
        max_length = 30
    )

    father_name = models.CharField(
        blank = True,
        max_length = 70
    )
    father_occupation = models.CharField(
        blank = True,
        max_length = 30
    )

    height = models.PositiveIntegerField(
        verbose_name = 'Height (cm)'
    )
    weight = models.PositiveIntegerField(
        verbose_name = 'Weight (kg)'
    )
    religion = models.CharField(
        blank = True,
        max_length = 30
    )

    def __str__(self):
        if self.middle_name:
            return f'{self.first_name} {self.middle_name[0]}. {self.last_name}' #pylint: disable=unsubscriptable-object
        return f'{self.first_name} {self.last_name}'

class Customer(Person):
    date_registered = models.DateField(
        auto_now_add = True
    )
    date_modified = models.DateField(
        auto_now = True
    )

