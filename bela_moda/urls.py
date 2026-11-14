from django.urls import path
from bela_moda.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = "bela_moda"

urlpatterns = [
    path("listar/", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/ver/", ProductDetailView.as_view(), name="product_detail"),
    path("criar/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/editar/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/deletar/", ProductDeleteView.as_view(), name="product_delete"),
]
