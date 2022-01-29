from django import template

register = template.Library()

# adapted from: https://django.cowhite.com/blog/numeric-for-loop-in-django-templates/


@register.filter(name="range")
def custom_range(int):
    """ 
    Takes in a integer and converts it 
    into an iterable list of numbers, starting from 1
    """
    return range(1, int + 1)