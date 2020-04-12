from django.shortcuts import render

# Create your views here.
def main(request):
    value = {
        'title': 'Главная',
        'content_class': 'slider'
    }
    return render(request, 'index.html', value)

def products(request):
    value = {
        'title': 'Каталог',
        'content_class': 'hero-white'
    }
    return render(request, 'products.html', value)

def contacts(request):
    value = {
        'title': 'Контакты',

        'content_class': 'hero'
    }
    return render(request, 'contact.html', value)

def test(request):
    value = {
        'title' : 'HORROR',
        'content_class' : 'hero'
    }
    return render(request, 'test.html', value)