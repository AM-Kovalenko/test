from django.db import models


class Contract(models.Model):
    """Контракт"""
    name = models.CharField("Контракт", max_length=150)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


class Manufacturer(models.Model):
    """Производитель"""
    name = models.CharField("Производитель", max_length=150)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


class Product(models.Model):
    """Товар"""
    name = models.CharField("Товар", max_length=150)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


class CreditApplication(models.Model):
    """Кредитная заявка"""
    name = models.CharField("Заявка", max_length=150)
    сontract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    product_list = models.ManyToManyField(Product)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
