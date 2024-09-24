from django.shortcuts import render


def home(request):
    # Представление для главной страницы
    return render(request, 'home.html')


def data(request):
    # Представление для страницы data
    return render(request, 'data.html')


def test(request):
    # Представление для страницы test
    return render(request, 'test.html')