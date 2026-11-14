from django import forms
from bela_moda.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "stock",
            "size",
            "brand",
            "image",
        ]