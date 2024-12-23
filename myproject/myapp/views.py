from django.shortcuts import render


def home(request):
    # Представление для главной страницы
    data = {
        'caption': "Переменная из <views.py>"
    }
    return render(request, 'myapp/home.html', data)


def data(request):
    # Представление для страницы data
    data = {
        'caption': "Переменная из <views.py>"
    }
    return render(request, 'myapp/data.html', data)


def test(request):
    # Представление для страницы test
    data = {
        'caption': "Переменная из <views.py>"
    }
    return render(request, 'myapp/test.html', data)

def test2(request):
    # Представление для страницы test2
    data = {
        'caption': "Переменная из <views.py>"
    }
    return render(request, 'myapp/test2.html', data)