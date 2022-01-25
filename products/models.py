from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Shoe(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    brand = models.ForeignKey('Brand',
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name