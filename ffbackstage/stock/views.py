from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView

from .forms import *
from .models import *
from .services.filter_products import filter_products
from .utils import MenuMixin, menu


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


class ListProducts(MenuMixin, ListView):
    template_name = 'stock/products.html'
    context_object_name = 'products'
    title_page = 'название страницы'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список товаров'
        context['form'] = ProductFilterForm(self.request.GET)
        return self.get_mixin_content(context)

    def get_queryset(self):
        form = ProductFilterForm(self.request.GET)
        if form.is_valid():
            return filter_products(form)


class ShowProduct(MenuMixin, DetailView):
    model = Products
    template_name = 'stock/product_card.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_content(context, title=context['product'].name)


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
