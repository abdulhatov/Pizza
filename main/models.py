from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    email = models.EmailField(_('email address'),  unique=True)

    def __str__(self):
        return self.email


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name_p = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name_p

class Pizza(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='ingredient')
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


