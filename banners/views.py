from django.shortcuts import render


def banner_maintenance(request):
    template = 'banners/maintenance.html'

    return render(request, template)


def create_banner(request):
    pass


def edit_banner(request, banner_id):
    pass


def delete_banner(request, banner_id):
    pass
