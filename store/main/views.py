from django.shortcuts import render


def index(request):
    data = {'title': 'Greenhouse'}
    return render(request, 'main/index.html', data)


def about(request):
    data = {'title': 'О нас'}
    return render(request, 'main/about.html', data)


def contact(request):
    data = {'title': 'Контакты'}
    return render(request, 'main/contact.html', data)
