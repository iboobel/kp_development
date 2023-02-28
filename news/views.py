from django.shortcuts import render
from django.http import HttpResponse
from .models import New, Category


def hello(request):
    return HttpResponse("Hello, world.")

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'all_categories.html', {'categories': categories})


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    news = New.objects.filter(categories=category)
    return render(request, 'category.html', {'news': news, 'category': category })


def news_detail(request, news_id):
    news = New.objects.get(id=news_id)
    return render(request, 'news_detail.html', {'news': news})








#
#
#
# - Категорії
# - Новини (в категорії)
# - Детальна сторінка новини

