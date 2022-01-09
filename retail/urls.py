from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buy', views.buy_product_form),
    path('buytransaction', views.buy_product),
    path('sell', views.sell_product_form),
    path('selltransaction', views.sell_product),
    path('newproducttype', views.product_type_form),
    path('newproducttypeadded', views.product_type_save),
    path('listproducttypes', views.product_type_list),
    path('newproduct', views.product_form),
    path('newproductadded', views.product_save),
    path('listproducts', views.product_list),
    path('buyhistory', views.buy_history),
    path('sellhistory', views.sell_history),
    path('product-json/<str:pt>/', views.get_json_product_data),
    path('productdelete', views.product_delete_form),
    path('productdeleted', views.product_delete),
    path('producttypedelete', views.product_type_delete_form),
    path('producttypedeleted', views.product_type_delete),
]
