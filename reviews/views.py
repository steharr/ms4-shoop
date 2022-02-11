from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Review
from products.models import Shoe
from .forms import ReviewForm

# Create your views here.
# Register your models here.


# read reviews view
def view_reviews(request, shoe_id):
    """ 
    A view to allow users
    to view the reviews for a specific shoe 
    """

    shoe = get_object_or_404(Shoe, pk=shoe_id)
    reviews = Review.objects.filter(shoe__pk=shoe_id)

    context = {'shoe': shoe, 'reviews': reviews}

    template = 'reviews/product_reviews.html'

    return render(request, template, context)


# write reviews
@login_required
def write_review(request, shoe_id):
    """ 
    A view to allow users
    to write a review for a specific shoe 
    """
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    prefill = {
        'shoe': shoe,
        'user': request.user,
    }
    # post handler for submitting reviews
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect(reverse('view_reviews', args=[shoe_id]))
        else:
            pass

    # render form with prefilled data
    review_form = ReviewForm(initial=prefill)
    review_form.fields['shoe'].disabled = True
    review_form.fields['user'].disabled = True
    context = {
        'shoe': shoe,
        'review_form': review_form,
    }

    template = 'reviews/write_review.html'

    return render(request, template, context)


# edit reviews
@login_required
def edit_review(request, shoe_id):

    # get the user
    user = request.user

    # get the associated review
    review = Review.objects.filter(user=user).filter(shoe__id=shoe_id)

    pass


# delete reviews
@login_required
def delete_review(request, shoe_id):
    pass