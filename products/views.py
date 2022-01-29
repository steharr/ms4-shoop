from django.shortcuts import get_object_or_404, render
from .models import Shoe


def all_shoes(request):
    """ A view to allow user to browse, sort and search shoes """

    shoes = Shoe.objects.all()

    context = {
        'shoes': shoes,
    }

    template = 'products/browse.html'

    return render(request, template, context)


def shoe_detail(request, shoe_id):
    """ A view to allow user to look at specific shoe """

    shoe = get_object_or_404(Shoe, pk=shoe_id)

    context = {
        'shoe': shoe,
    }

    template = 'products/detail.html'

    return render(request, template, context)
