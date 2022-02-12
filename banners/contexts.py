from .models import Banner


def sales_banners(request):

    banner = Banner.objects.get(
        pk=3)  # there should only ever be one banner pk=1
    if banner:
        full_banner_message = f"{banner.message}: {str(banner.discount)}% off all orders over &euro; {str(banner.price_threshold)}"
        banner_context = {
            'message': banner.message,
            'theme': banner.theme,
            'discount': banner.discount,
            'price_threshold': banner.price_threshold,
            'full_banner_message': full_banner_message,
        }
    else:
        banner_context = {}

    context = {'banner': banner_context}
    return context
