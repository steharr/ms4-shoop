from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Shoe


def view_cart(request):
    """ View for user to see whats in their shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, shoe_id):
    """ Add a specified shoe to the cart """

    # extract the cart object
    cart = request.session.get('cart', {})

    shoe = get_object_or_404(Shoe, pk=shoe_id)
    size = request.POST.get('shoe_size')
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


def remove_from_cart(request, shoe_id):
    """ Remove a specified shoe in the cart """
    try:
        # extract the cart object
        cart = request.session.get('cart', {})

        # find the specified size  from the request
        size = request.POST['size']

        # remove the specified size in the server cart variable
        del cart[shoe_id][size]

        # update the client session cart
        request.session['cart'] = cart

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


def update_cart(request, shoe_id):
    """ update the qty of a specified shoe in the cart """
    try:
        # extract the cart object
        cart = request.session.get('cart', {})

        # find the specified size and new qty from the request
        size = request.POST['size']
        new_qty = request.POST['qty']

        # update the server cart variable with new qty
        cart[shoe_id][size] = {'qty': int(new_qty)}

        # update the client session cart
        request.session['cart'] = cart

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
