from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bela_moda.forms import ProductForm
from bela_moda.models import Product, Brand


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = "bela_moda/product_list.html"
    context_object_name = "products"
    paginate_by = 10
    permission_required = "bela_moda.view_product"

    def get_queryset(self):
        queryset = Product.objects.all()
        marca = self.request.GET.get("marca")

        if marca:
            queryset = queryset.filter(brand_id=marca)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        context["selected_brand"] = self.request.GET.get("marca", "")
        return context


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = "bela_moda/product_detail.html"
    context_object_name = "product"
    permission_required = "bela_moda.view_product"


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "bela_moda/product_form_create.html"
    success_url = reverse_lazy("bela_moda:product_list")
    permission_required = "bela_moda.add_product"


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "bela_moda/product_form_update.html"
    context_object_name = "product"
    success_url = reverse_lazy("bela_moda:product_list")
    permission_required = "bela_moda.change_product"


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "bela_moda/product_confirm_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("bela_moda:product_list")
    permission_required = "bela_moda.delete_product"
