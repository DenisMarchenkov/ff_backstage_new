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


class MenuMixin:
    def get_mixin_content(self, context, **kwargs):
        context['menu'] = menu
        context.update(kwargs)
        return context
