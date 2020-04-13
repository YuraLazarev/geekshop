from django.shortcuts import render
from .models import Product

# Create your views here.
def main(request):
    products = Product.objects.all()[:4]
    value = {
        'title': 'Главная',
        'content_class': 'slider',
        'products': products
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

def products(request, pk=None):
    if pk:
        product_item = Product.objects.get(pk=pk)

    # prod_menu = [
    #     {'href':'products_all', 'name':'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]
    value = {
        #'links_menu': prod_menu,
        'title': 'Каталог',
        'content_class': 'hero-white',
        'product_item': product_item
    }
    return render(request, 'products.html', value)

def products_all(request, pk=None):

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