from .models import Banner


def sale_banner(request):
    banner = request.session.get('banner', {})
    context = {'banner': banner}

    return context