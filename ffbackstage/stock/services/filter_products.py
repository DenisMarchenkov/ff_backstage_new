from django.db.models import Q

from stock.models import Products


def filter_products(form):
    #prod = que
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
    print(type(prod))
    return prod
