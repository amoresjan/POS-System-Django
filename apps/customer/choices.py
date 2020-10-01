from django.db import models

class Gender(models.TextChoices):
    Male = ('M', 'Male')
    Female = ('F', 'Female')
    Others = ('O', 'Others')

class Status(models.TextChoices):
    Single = ('S', 'Single')
    Married = ('M', 'Married')
    Widowed = ('W', 'Widowed')
    Divorced = ('D', 'Divorced')