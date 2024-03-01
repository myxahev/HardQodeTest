from django.urls import path
from src.rest.views import product_list_api, lesson_list_by_product_api, product_statistics_api

urlpatterns = [
    path('api/products/', product_list_api, name='product-list'),
    path('api/products/<int:product_id>/lessons/', lesson_list_by_product_api, name='lesson-list-by-product'),
    path('api/product-statistics/', product_statistics_api, name='product-statistics'),
]
