from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.all()
    categories = Categories.objects.all()
    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'index.html', context=context)


def categories(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Categories.objects.all()
    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'categories.html', context=context)


def new_about(request, new_id):
    news = News.objects.get(pk=new_id)
    categories = Categories.objects.all()
    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'new_about.html', context=context)
