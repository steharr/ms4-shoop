from django.shortcuts import render, redirect
from .forms import BannerForm
from .models import Banner
from django.contrib import messages
from django.urls import reverse


def banner_maintenance(request):
    template = 'banners/maintenance.html'
    return render(request, template)


def create_banner(request):

    # post handler
    if request.method == "POST":
        banner_form = BannerForm(request.POST)
        if banner_form.is_valid():
            # delete existing banners
            Banner.objects.all().delete()
            # save new banner
            banner_form.save()
            messages.success(request, "Sales banner added to site!")
            return redirect(reverse('banner_maintenance'))
        else:
            messages.warning(request,
                             "Error creating sales banner, please try again")
            return redirect(reverse('banner_maintenance'))

    banner_form = BannerForm()
    context = {'banner_form': banner_form}
    template = 'banners/create_banner.html'
    return render(request, template, context)


def edit_banner(request, banner_id):
    pass


def delete_banner(request, banner_id):
    pass
