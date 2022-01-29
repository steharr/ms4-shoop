from django.shortcuts import render, get_object_or_404
from .models import Review
from products.models import Shoe

# Create your views here.
# Register your models here.


# read reviews view
def view_reviews(request, shoe_id):
    """ A view to allow user to browse, sort and search shoes """

    shoe = get_object_or_404(Shoe, pk=shoe_id)
    reviews = Review.objects.filter(shoe__pk=shoe_id)

    context = {'shoe': shoe, 'reviews': reviews}

    template = 'reviews/product_reviews.html'

    return render(request, template, context)


# write reviews

# edit reviews

# delete reviews
