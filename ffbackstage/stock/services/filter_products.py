from django.db.models import Q

from stock.models import Products


def filter_products(form):
    prod = Products.objects.all()

    if form.cleaned_data['brand']:
        prod = prod.filter(brand__in=form.cleaned_data['brand'])

    if form.cleaned_data['search_field']:
        search = form.cleaned_data['search_field']
        if prod.filter(name__icontains=search).exists():
            prod = prod.filter(name__icontains=search)
        elif prod.filter(code__icontains=search).exists():
            prod = prod.filter(code__icontains=search)
        else:
            prod = prod.filter(article__icontains=search)

    if form.cleaned_data['tag']:
        prod = prod.filter(tags__in=form.cleaned_data['tag']).distinct()

    if form.cleaned_data['supplied']:
        supplied = form.cleaned_data['supplied']
        if len(supplied) > 1:
            prod = prod.filter(Q(is_supplied=supplied[0]) | Q(is_supplied=supplied[1]))
        else:
            prod = prod.filter(is_supplied=supplied[0])

    if form.cleaned_data['active']:
        active = form.cleaned_data['active']
        if len(active) > 1:
            prod = prod.filter(Q(is_active=active[0]) | Q(is_active=active[1]))
        else:
            prod = prod.filter(is_active=active[0])

    if form.cleaned_data['promo']:
        promo = form.cleaned_data['promo']
        if len(promo) > 1:
            prod = prod.filter(Q(is_promo=promo[0]) | Q(is_promo=promo[1]))
        else:
            prod = prod.filter(is_promo=promo[0])
    return prod


def filter_products_new(form):
    filters = form.cleaned_data
    for k, v in filters.copy().items():
        if v == '' or len(v) < 1:
            filters.pop(k)
        else:
            filters.pop(k)
            if k == 'brand':
                filters[f'{k}__in'] = v
            if k == 'tag':
                filters[f'{k}s__in'] = v
            if k == 'search_field':
                filters['name__icontains'] = v
            if k == 'active':
                if len(v) > 1:
                    pass
                else:
                    filters['is_active'] = v[0]
            if k == 'promo':
                if len(v) > 1:
                    pass
                else:
                    filters['is_promo'] = v[0]
            if k == 'supplied':
                if len(v) > 1:
                    pass
                else:
                    filters['is_supplied'] = v[0]

    result = Products.objects.filter(**filters)
    if result.exists():
        return result.distinct()
    else:
        result = Products.objects.filter(code__icontains=filters['name__icontains'])
        if result.exists():
            return result
        else:
            result = Products.objects.filter(article__icontains=filters['name__icontains'])
            return result

