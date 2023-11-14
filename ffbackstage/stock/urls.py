from django.urls import path, include
from . import views

app_name = 'stock'

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('', views.stock_main, name='stock'),
    path('credit/', views.credit, name='credit'),
    path('debit/', views.debit, name='debit'),
    path('products/', views.products, name='products'),
    #path('products/', views.ListProducts.as_view(), name='products'),
    path('products/<slug:product_slug>/', views.ShowProduct.as_view(), name='product_card'),
    path('brands/', views.brand_card, name='brand_card'),
    path('test/', views.test, name='test'),
    # path('tag/<slug:tag_slug>/', views.show_tag_products_list, name='tag'),
    # path('brands/<int:brand_id>/', views.show_brand, name='brand_card'),
    # path('brand/<slug:brand_slug>/', views.show_brand, name='brands'),
]

