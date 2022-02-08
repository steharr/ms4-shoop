import uuid
from django.db import IntegrityError, models
from django.db.models import Sum
from products.models import Shoe


class Order(models.Model):

    ORDER_STATUS_CHOICES = (('A', 'Created'), ('B', 'Payed For'),
                            ('C', 'In Transit'), ('D', 'Complete'))

    # order reference details
    order_number = models.CharField(max_length=32, editable=False)
    order_date = models.DateField(auto_now_add=True)

    # personal details
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)

    # address details
    street1 = models.CharField(max_length=80)
    street2 = models.CharField(null=True, blank=True, max_length=80)
    town_or_city = models.CharField(null=True, blank=True, max_length=50)
    county = models.CharField(null=True, blank=True, max_length=80)
    postcode = models.CharField(max_length=20)
    country = models.CharField(null=True, blank=True, max_length=80)

    # payment details
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      default=0)
    delivery_cost = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      default=0)

    # order status details
    order_status = models.CharField(max_length=1,
                                    choices=ORDER_STATUS_CHOICES,
                                    default='A')

    def _generate_order_number(self):
        """
        Generates a string of 25 random characters
        """
        return str(uuid.uuid4().int)[:25]

    def update_grand_total(self):
        """
        Updates the order grand total
        when triggered
        """
        self.order_total = self.line_items.aggregate(Sum('item_total'))
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Overrides default save method
        to add unique order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):

    # order reference details
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name="line_items")

    shoe = models.ForeignKey(Shoe,
                             on_delete=models.CASCADE,
                             related_name="line_items")
    size = models.CharField(max_length=3)
    qty = models.IntegerField(default=0)
    item_total = models.DecimalField(max_digits=10,
                                     decimal_places=2,
                                     editable=False)

    def save(self, *args, **kwargs):
        """
        Overrides the default to save
        to update the line item price
        """
        self.item_total = self.shoe.price * self.qty
        super().save(self, *args, **kwargs)

    def __str__(self):
        return f'Order Number: {self.order.order_number}, Item: {self.id}'
