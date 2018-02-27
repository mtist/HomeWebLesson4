from django.shortcuts import render
from .models import Page


def home(request):
    pages = Page.objects.all()
    return render(request, 'home.html', {'pages': pages})


def pages(request, slug):
    page = Page.objects.get(slug=slug)
    page_list = Page.objects.all()
    return render(request, 'page.html', {'page': page, 'pages': page_list})
