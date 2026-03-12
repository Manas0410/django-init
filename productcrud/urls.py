from django.urls import path
from .views import *

urlpatterns = [

    path("products/", get_products),

    path("products/<int:id>/", get_product),

    path("products/add/", add_product),

    path("products/update/<int:id>/", update_product),

    path("products/delete/<int:id>/", delete_product),

]