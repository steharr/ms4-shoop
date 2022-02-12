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


def edit_banner(request):

    banner = Banner.objects.get()

    # post handler
    if request.method == "POST":
        banner_form = BannerForm(request.POST, instance=banner)
        if banner_form.is_valid():
            # save new banner
            banner_form.save()
            messages.success(request, "Sales banner edited successfully!")
            return redirect(reverse('banner_maintenance'))
        else:
            messages.warning(request,
                             "Error editing sales banner, please try again")
            return redirect(reverse('banner_maintenance'))

    banner_form = BannerForm(instance=banner)
    context = {'banner_form': banner_form, 'banner': banner}
    template = 'banners/edit_banner.html'

    return render(request, template, context)


def delete_banner(request):
    if Banner.objects.all().count() > 0:
        Banner.objects.all().delete()
        messages.info(request, "Sales banner deleted")
    else:
        messages.warning(request, "No banner available to delete")
    return redirect(reverse('banner_maintenance'))
