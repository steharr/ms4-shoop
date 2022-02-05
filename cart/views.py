from django.shortcuts import render, get_object_or_404, redirect
from products.models import Shoe


def view_cart(request):
    """ View for user to see whats in their shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, shoe_id):
    """ Add a specified shoe to the cart """
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    size = request.POST.get('shoe_size')
    cart = request.session.get('cart', {})
    redirect_url = request.POST.get('redirect_url')

    # check if shoe is already in the cart
    if shoe_id in list(cart.keys()):
        # check if size already exist in cart
        if size in list(cart[shoe_id]):
            cart[shoe_id][size]['qty'] += 1
        else:
            # init an empty size object
            cart[shoe_id][size] = {}
            cart[shoe_id][size]['qty'] = 1
    else:
        # init an empty shoe object
        cart[shoe_id] = {}
        # init an empty size object
        cart[shoe_id][size] = {}
        cart[shoe_id][size]['qty'] = 1

    request.session['cart'] = cart
    return redirect(redirect_url)
