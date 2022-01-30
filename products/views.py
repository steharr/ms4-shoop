from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Shoe
from django.db.models import Q


def all_shoes(request):
    """ A view to allow user to browse, sort and search shoes """

    # get handler
    if request.GET:
        # search box queries
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # error messages -> empty query
                return redirect(reverse('products'))
            # search for specified text in name or descript
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            shoes = Shoe.objects.filter(queries)
        else:
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
