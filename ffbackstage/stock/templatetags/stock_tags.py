from django import template
from django.db.models import Count
from django.shortcuts import get_object_or_404

from stock.models import *


register = template.Library()


@register.inclusion_tag('stock/list_brands.html')
def show_brands(brand_selected=0):
    brands = Brands.objects.all()
    # brands = Brands.objects.annotate(total=Count('brand')).filter(total__gt=0)
    return {'brands': brands, 'brand_selected': brand_selected}


@register.inclusion_tag('stock/list_tags.html')
def show_all_tags():
    return {'tags': TagsProducts.objects.all()}
    # tags = TagsProducts.objects.annotate(total=Count('tags')).filter(total__gt=0)
    return {'tags': tags}
