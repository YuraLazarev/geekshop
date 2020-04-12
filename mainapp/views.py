from django.shortcuts import render

# Create your views here.
def main(request):
    value = {
        'title': 'Главная',
        'content_class': 'slider'
    }
    return render(request, 'index.html', value)



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

def products(request):
    prod_menu = [
        {'href':'products_all', 'name':'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    value = {
        'links_menu': prod_menu,
        'title': 'Каталог',
        'content_class': 'hero-white'
    }
    return render(request, 'products.html', value)

def products_all(request):
    prod_menu = [
        {'href':'products_all', 'name':'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    value = {
        'links_menu': prod_menu,
        'title': 'Каталог',
        'content_class': 'hero-white'
    }
    return render(request, 'products.html', value)

def products_home(request):
    prod_menu = [
        {'href':'products_all', 'name':'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    value = {
        'links_menu': prod_menu,
        'title': 'Каталог',
        'content_class': 'hero-white'
    }
    return render(request, 'products.html', value)

def products_office(request):
    prod_menu = [
        {'href':'products_all', 'name':'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    value = {
        'links_menu': prod_menu,
        'title': 'Каталог',
        'content_class': 'hero-white'
    }
    return render(request, 'products.html', value)

def products_modern(request):
    prod_menu = [
        {'href':'products_all', 'name':'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    value = {
        'links_menu': prod_menu,
        'title': 'Каталог',
        'content_class': 'hero-white'
    }
    return render(request, 'products.html', value)

def products_classic(request):
    prod_menu = [
        {'href':'products_all', 'name':'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    value = {
        'links_menu': prod_menu,
        'title': 'Каталог',
        'content_class': 'hero-white'
    }
    return render(request, 'products.html', value)