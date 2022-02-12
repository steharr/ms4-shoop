from .models import Banner


def sales_banners(request):

    try:
        banner = Banner.objects.get(
        )  # there should only ever be one banner in db
        full_banner_message = f"{banner.message}: {str(banner.discount)}% off all orders over &euro; {str(banner.price_threshold)}"
        banner_context = {
            'message': banner.message,
            'theme': banner.theme,
            'discount': banner.discount,
            'price_threshold': banner.price_threshold,
            'full_banner_message': full_banner_message,
        }
    except:
        banner_context = {}

    context = {'banner': banner_context}
    return context
