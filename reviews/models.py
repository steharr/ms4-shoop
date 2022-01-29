from django.db import models
from products.models import Shoe
from django.contrib.auth.models import User


class Review(models.Model):
    # once shoe deleted, all reviews removed
    # shoe needed for review
    shoe = models.ForeignKey(Shoe,
                             null=False,
                             blank=False,
                             on_delete=models.CASCADE)

    # user can be deleted but still review remain
    # user not needed to review
    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             on_delete=models.SET_NULL)
    rating = models.DecimalField(decimal_places=1,
                                 max_digits=2,
                                 null=False,
                                 blank=False)
    details = models.TextField(null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
