from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contact, index, product_detail, product_create


app_name = "catalog"

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact, name="contact"),
    path("index/", index),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path("product/create/", product_create, name="product_create"),

]