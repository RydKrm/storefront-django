from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("list", views.product_list),
    path("singleProduct/<int:id>", views.single_product),
    path('collections/<int:pk>', views.collection_details, name='collection-detail'),
    path('customer/<int:id>', views.store_customer),
    path('product/<int:id>',views.ProductList.as_view())

]