from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewForm
from .models import *
from django.db.models import *


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
        'new': news,
        'categories': categories,
    }
    return render(request, 'new_about.html', context=context)


#
# def add_news(request):
#     if request.method == 'POST':
#         form = NewForm(request.POST, request.FILES)
#         if form.is_valid():
#             news = News.objects.create(**form.cleaned_data)
#             return redirect('home')
#     else:
#         form= NewForm()
#     return render(request, 'add_news.html', context={'form': form})

def add_news(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect('home')

    else:
        form = NewForm()
    return render(request, 'add_news.html', context={'form': form})


def update_new(request, new_id):
    new = get_object_or_404(News, id=new_id)
    if request.method == 'POST':
        form = NewForm(request.POST, instance=new)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            form.save()
            return redirect('home')

    else:
        form = NewForm(instance=new)
    return render(request, 'update_new.html', context={'form': form, 'new': new})





def search_view(request):
    query = request.GET.get('q', '')  # Foydalanuvchidan qidiruv so‘rovini olish
    results = News.objects.filter(
        Q(title__icontains=query) |
        Q(context__icontains=query)
    ) if query else News.objects.all()

    return render(request, 'search_news.html', {'news_list': results, 'query': query})

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news_detail.html', {'news': news})