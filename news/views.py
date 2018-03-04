from django.shortcuts import render
from .models import Article


def news_list(request):
    news = Article.objects.all()
    return render(request, 'news_list.html', {'news_detail': news})


def news_detail(request, slug):
    news = Article.objects.get(slug=slug)
    news_list = Article.objects.all()
    return render(request, 'news.html', {'new': news, 'news': news_list})
