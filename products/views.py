from django.shortcuts import render
from .models import Shoe


def all_shoes(request):
    """ A view to allow user to browse, sort and search shoes """

    shoes = Shoe.objects.all()

    context = {
        'shoes': shoes,
    }

    return render(request, 'products/browse.html', context)
