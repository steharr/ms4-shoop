from django.shortcuts import render
from .forms import BannerForm


def banner_maintenance(request):
    template = 'banners/maintenance.html'
    return render(request, template)


def create_banner(request):
    banner_form = BannerForm()
    context = {'banner_form': banner_form}
    template = 'banners/create_banner.html'
    return render(request, template, context)


def edit_banner(request, banner_id):
    pass


def delete_banner(request, banner_id):
    pass
