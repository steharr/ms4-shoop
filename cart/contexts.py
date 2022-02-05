from products.models import Shoe
from django.shortcuts import get_object_or_404


def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0

    for shoe_id, shoe_data in cart.items():
        shoe = get_object_or_404(Shoe, pk=shoe_id)
        for chosen_size in shoe_data:
            qty = shoe_data[chosen_size]['qty']
            item_price = shoe.price * qty
            grand_total += item_price
            cart_items.append({
                'shoe_id': shoe_id,
                'shoe': shoe,
                'size': chosen_size,
                'qty': qty,
                'item_price': item_price
            })
    context = {'cart_items': cart_items, 'grand_total': grand_total}

    return context