from django.db import models


class Banner(models.Model):
    THEME_CHOICES = (('U', 'Urgent'), ('M', 'Moderate'), ('L', 'Reminder'))
    message = models.CharField(max_length=254)
    theme = models.CharField(max_length=1)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    price_threshold = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name