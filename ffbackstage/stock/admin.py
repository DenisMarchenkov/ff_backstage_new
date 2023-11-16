from simple_history.admin import SimpleHistoryAdmin
from django.contrib import admin
from .models import *


@admin.register(Products)
class ProductsAdmin(SimpleHistoryAdmin):
    list_display = ('code', 'article', 'name', 'unit', 'is_active', 'is_supplied', 'is_promo',)
    list_per_page = 17
    search_fields = ('code', 'article', 'name')
    filter_horizontal = ['tags']
    prepopulated_fields = {'slug': ('name',)}
    exclude = ('author',)

    history_list_display = [
    ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Brands)
class BrandsAdmin(SimpleHistoryAdmin):
    list_display = ('name_short', 'discount', 'markup', 'time_create')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(TagsProducts)
