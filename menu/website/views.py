from django.shortcuts import render
from .models import Menu, Under_menu

# Create your views here.
menus = Menu.objects.all()
under = Under_menu.objects.all()
context = {
    'menus': menus,
    'under_menus': under
}


def index(request):
    print(menus)
    print(under)

    return render(request, 'website/index.html', context)


def about(request):
    return render(request, 'website/about.html', context)


def news(request):
    return render(request, 'website/news.html', context)
