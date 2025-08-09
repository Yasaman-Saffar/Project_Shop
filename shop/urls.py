from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('add_product/', views.Add_products_view, name='add_product_page'),
    path('products/<slug:slug>' , views.product_details_view, name='product-details'),
    path('support/', views.support, name='support_page'),
]
