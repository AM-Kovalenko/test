from django.db import models


class Contract(models.Model):
    """Контракт"""
    name = models.CharField("Контракт", max_length=150)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    """Производитель"""
    name = models.CharField("Производитель", max_length=150)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар"""
    name = models.CharField("Товар", max_length=150)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name


class CreditApplication(models.Model):
    """Кредитная заявка"""
    name = models.CharField("Заявка", max_length=150)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='credits')
    product_list = models.ManyToManyField(Product, related_name='credit_applications')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name
