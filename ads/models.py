from django.db import models
from django.utils import timezone
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    image = models.ImageField(upload_to="images/", verbose_name="product image", **NULLABLE)
    title = models.CharField(max_length=255, verbose_name="product name")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="product price")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='product author', **NULLABLE)
    created_at = models.DateField(default=timezone.now, verbose_name="product creation date")
    description = models.TextField(verbose_name="product description")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    pass
