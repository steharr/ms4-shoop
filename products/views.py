from unicodedata import category
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Shoe, Brand, Category
from reviews.models import Review
from django.db.models import Q, Avg, Count
from django.contrib import messages


def all_shoes(request):
    """ A view to allow user to browse, sort and search shoes """
    shoes = Shoe.objects.all()
    header = "Browse - All"
    categories = Category.objects.all()
    brands = Brand.objects.all()

    # get handler
    if request.GET:

        # search box queries
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # error messages -> empty query
                messages.info(request, "No input text given for search!")
                return redirect(reverse('shoes'))
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
                header = 'Browse - Mens'
            else:
                header = 'Browse - Womens'

    # initialise a refined search variable
    refined_search = {}

    # handle refined searches
    if 'filter_category' in request.GET:
        query = request.GET['filter_category']
        if query != 'all':
            category = Category.objects.get(name=query)
            shoes = shoes.filter(category=category)
            refined_search['category'] = query
        else:
            refined_search['category'] = 'All'

    if 'filter_brand' in request.GET:
        query = request.GET['filter_brand']
        if query != 'all':
            brand = Brand.objects.get(name=query)
            shoes = shoes.filter(brand=brand)
            refined_search['brand'] = query
        else:
            refined_search['brand'] = 'All'

    if 'sort_price' in request.GET:
        query = request.GET['sort_price']
        if query == 'desc':
            shoes = shoes.order_by('-price')
            refined_search['sort_price'] = 'High to Low'
        elif query == 'asc':
            shoes = shoes.order_by('price')
            refined_search['sort_price'] = 'Low to High'
        else:
            refined_search['sort_price'] = 'Reset'

    # annotate shows with average ratings & review count
    shoes = shoes.annotate(avg_rating=Avg('review__rating'),
                           count_reviews=Count('review'))

    if 'sort_rating' in request.GET:
        query = request.GET['sort_rating']
        if query == 'desc':
            shoes = shoes.order_by('-avg_rating')
            refined_search['sort_rating'] = 'High to Low'
        elif query == 'asc':
            shoes = shoes.order_by('avg_rating')
            refined_search['sort_rating'] = 'Low to High'
        else:
            refined_search['sort_rating'] = 'Reset'

    context = {
        'shoes': shoes,
        'header': header,
        'categories': categories,
        'brands': brands,
        'refined_search': refined_search,
    }

    template = 'products/browse.html'

    return render(request, template, context)


def shoe_detail(request, shoe_id):
    """ A view to allow user to look at specific shoe """

    # find average ratings for the extracted shoe
    shoe = Shoe.objects.annotate(
        avg_rating=Avg('review__rating'),
        count_reviews=Count('review'),
    ).get(pk=shoe_id)

    context = {
        'shoe': shoe,
    }

    template = 'products/detail.html'

    return render(request, template, context)
