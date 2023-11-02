from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .forms import *
from .models import *

menu = [
    {'title': 'Home', 'url_name': 'stock:stock'},
    {'title': 'Debit', 'url_name': 'stock:debit'},
    {'title': 'Credit', 'url_name': 'stock:credit'},
    {'title': 'Products', 'url_name': 'stock:products'},
    {'title': 'Brands', 'url_name': 'stock:brand_card'},
    {'title': 'test', 'url_name': 'stock:test'},
    {'title': 'login', 'url_name': 'users:login'},
    {'title': 'logout', 'url_name': 'users:logout'},
]


def home(request):
    data = {'menu': menu,
            'title': 'Главная страница'
            }
    return render(request, 'stock/home.html', context=data)


def stock_main(request):
    data = {'menu': menu,
            'title': 'Главная страница приложения STOCK'
            }
    return render(request, 'stock/stock_index.html', context=data)


def credit(request):
    data = {'menu': menu,
            'title': 'Страница РАСХОДА товаров'
            }
    return render(request, 'stock/credit.html', context=data)


def debit(request):
    data = {'menu': menu,
            'title': 'Страница ПРИХОДА товаров'
            }
    return render(request, 'stock/debit.html', context=data)


def products(request):
    form = ProductFilterForm(request.GET)
    products = Products.objects.all()

    if form.is_valid():
        if form.cleaned_data['brand']:
            products = products.filter(brand__in=form.cleaned_data['brand'])

        if form.cleaned_data['search_field']:
            search = form.cleaned_data['search_field']
            if products.filter(name__icontains=search).exists():
                products = products.filter(name__icontains=search)
            elif products.filter(code__icontains=search).exists():
                products = products.filter(code__icontains=search)
            else:
                products = products.filter(article__icontains=search)

        if form.cleaned_data['tag']:
            products = products.filter(tags__in=form.cleaned_data['tag']).distinct()

        if form.cleaned_data['supplied']:
            supplied = form.cleaned_data['supplied']
            if len(supplied) > 1:
                products = products.filter(Q(is_supplied=supplied[0]) | Q(is_supplied=supplied[1]))
            else:
                products = products.filter(is_supplied=supplied[0])

        if form.cleaned_data['active']:
            active = form.cleaned_data['active']
            if len(active) > 1:
                products = products.filter(Q(is_active=active[0]) | Q(is_active=active[1]))
            else:
                products = products.filter(is_active=active[0])

        if form.cleaned_data['promo']:
            promo = form.cleaned_data['promo']
            if len(promo) > 1:
                products = products.filter(Q(is_promo=promo[0]) | Q(is_promo=promo[1]))
            else:
                products = products.filter(is_promo=promo[0])

    data = {
        'menu': menu,
        'title': 'Все товары',
        'products': products,
        'form': form
    }
    return render(request, 'stock/products.html', context=data)


def show_product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    tags = product.tags.filter()
    data = {
        'title': product.name,
        'menu': menu,
        'product': product,
        'tags': tags,
        # 'brand_selected': 0,
        # 'product_slug': product_slug
    }
    return render(request, 'stock/product_card.html', context=data)


def brand_card(request):
    brands = Brands.objects.all()

    data = {'menu': menu,
            'title': 'Все марки',
            'body': brands
            }
    return render(request, 'stock/brands.html', context=data)


def test(request):
    products = Products.objects.all()
    form = ProductFilterForm(request.GET)
    data = {'menu': menu,
            'title': 'Тестовая страница',
            'form': form,
            'products': products
            }

    return render(request, 'stock/test.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def show_brand(request, brand_slug):
#     brand = get_object_or_404(Brands, slug=brand_slug)
#     products = Products.objects.filter(brand_id=brand.pk)
#
#     data = {
#         'menu': menu,
#         'title': f'Товары в марке: {brand.name}',
#         'products': products,
#         'sidebar': brand,
#         'brand_selected': brand.pk,
#     }
#     return render(request, 'stock/products.html', context=data)


# def show_tag_products_list(request, tag_slug):
#     tag = get_object_or_404(TagsProducts, slug=tag_slug)
#     products = tag.tags.filter()
#     print(products[0].brand.slug)
#
#     data = {
#         'menu': menu,
#         'title': f'Тег: {tag.tag}',
#         'products': products,
#         'brand_selected': None,
#         'tag_selected': tag.pk
#     }
#     return render(request, 'stock/products.html', context=data)