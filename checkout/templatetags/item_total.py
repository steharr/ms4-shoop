from django import template

register = template.Library()


@register.filter(name="item_total")
def item_total(price, qty):
    """
    Returns the item cost
    """
    return price * qty
