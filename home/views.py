from django.shortcuts import render


def index(request):
    """ View to show site index page """
    return render(request, 'home/index.html')
