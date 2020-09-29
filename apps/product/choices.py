from django.db import models

class Color(models.TextChoices):
    Black = ('B', 'Black')
    White = ('W', 'White')
    Red = ('R', 'Red')
    Green = ('G', 'Green')
    Yellow = ('Y', 'Yellow')
    Purple = ('P', 'Purple')
    Orange = ('O', 'Orange')
    
