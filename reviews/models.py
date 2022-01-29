from django.db import models
from products.models import Shoe
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    shoe = models.ForeignKey(Shoe,
                             null=False,
                             blank=False,
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    rating = models.IntegerField(
        null=False,
        blank=False,
        default=1,
        validators=[MaxValueValidator(5),
                    MinValueValidator(1)])
    details = models.TextField(null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
