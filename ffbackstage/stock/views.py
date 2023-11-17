from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView, UpdateView

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
    title_page = 'Список товаров'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


class AddProduct(MenuMixin, FormView):
    form_class = AddProductForm
    template_name = 'stock/add_product.html'
    success_url = reverse_lazy('stock:products')
    title_page = 'Добавление нового продукта'

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.author = self.request.user
        new_product.save()
        return super().form_valid(new_product)


class UpdateProduct(MenuMixin, UpdateView):
    model = Products
    fields = ['name', 'article', 'description']
    template_name = 'stock/add_product.html'
    title_page = 'Редактирование товара'
    success_url = reverse_lazy('stock:products')
    context_object_name = 'product'


class ListBrands(MenuMixin, ListView):
    template_name = 'stock/brands.html'
    context_object_name = 'brands'
    title_page = 'Список марок'

    def get_queryset(self):
        return Brands.objects.all().select_related('brand_prod')


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

