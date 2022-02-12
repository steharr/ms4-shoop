from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Banner(models.Model):
    THEME_CHOICES = (('U', 'Urgent'), ('M', 'Moderate'), ('L', 'Reminder'))
    message = models.CharField(max_length=254)
    theme = models.CharField(max_length=1, choices=THEME_CHOICES, default='U')
    discount = models.IntegerField(
        default=0, validators=[MaxValueValidator(30),
                               MinValueValidator(0)])
    price_threshold = models.DecimalField(max_digits=5, decimal_places=2)
