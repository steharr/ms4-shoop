from django.shortcuts import render, get_object_or_404, redirect
from products.models import Shoe


def view_cart(request):
    """ View for user to see whats in their shopping cart """
    template = ' cart/cart.html'
    return render(request, template)


def add_to_cart(request, shoe_id):
    """ Add a specified shoe to the cart """
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    size = request.POST.get('shoe_size')
    cart = request.session.get('cart', {})
    redirect_url = request.POST.get('redirect_url')

    if shoe_id in list(cart.keys()):  # check if shoe is already in the cart
        cart[shoe_id]['qty'] += 1
        cart[shoe_id]['size'] = size
    else:
        cart[shoe_id] = {}
        cart[shoe_id]['qty'] = 1
        cart[shoe_id]['size'] = size

    request.session['cart'] = cart
    return redirect(redirect_url)
