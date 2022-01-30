from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Shoe
from reviews.models import Review
from django.db.models import Q, Avg
from django.db.models.functions import Round


def all_shoes(request):
    """ A view to allow user to browse, sort and search shoes """
    shoes = Shoe.objects.all()
    header = "Browse - All"

    # get handler
    if request.GET:
        # search box queries
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # error messages -> empty query
                return redirect(reverse('products'))
            # search for text in name, description or category
            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                    category__name__icontains=query)
            shoes = shoes.filter(queries)
            header = f'Search - "{query}"'
        # gender queries
        if 'gender' in request.GET:
            gender = request.GET['gender']
            shoes = shoes.filter(gender__iexact=gender)
            if gender == "m":
                header = f'Browse - Mens'
            else:
                header = f'Browse - Womens'

    # find average ratings for all extracted shoes
    for extracted_shoe in shoes:
        avg_rating = Review.objects.filter(shoe=extracted_shoe).aggregate(
            Avg('rating'))
        if avg_rating['rating__avg'] is None:
            extracted_shoe.avg_rating = "No Reviews"
        else:
            extracted_shoe.avg_rating = round(avg_rating['rating__avg'])

    context = {
        'shoes': shoes,
        'header': header,
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
