from .models import Banner


def sales_banners(request):
    banner = request.session.get('banner', {})
    context = {'banner': banner}

    return context