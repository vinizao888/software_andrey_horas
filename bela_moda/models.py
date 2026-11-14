from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(verbose_name="Nome da marca", max_length=50)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    SIZE_CHOICES = [
        ("P", "Pequeno"),
        ("M", "Médio"),
        ("G", "Grande"),
        ("GG", "Extra grande"),
    ]

    name = models.CharField(verbose_name="Nome do produto", max_length=100)
    description = models.TextField(verbose_name="Descrição", blank=True)
    price = models.DecimalField(
        verbose_name="Preço (R$)",
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    stock = models.PositiveIntegerField(verbose_name="Quantidade em estoque", default=0)
    size = models.CharField(
        verbose_name="Tamanho",
        max_length=2,
        choices=SIZE_CHOICES,
        default="M",
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name="Marca",
    )
    image = models.ImageField(
        verbose_name="Foto",
        upload_to="bela_moda/images/",
        blank=True,
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["name"]

    def __str__(self):
        return self.name