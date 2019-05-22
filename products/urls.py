from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('products/search/', views.search_product, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<int:id>/<slug:slug>/like/', views.product_like, name='product_like'),
    path('<int:id>/<slug:slug>/rate/', views.product_rate, name='product_rate'),
]
