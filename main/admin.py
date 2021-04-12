from django.contrib import admin
from main.models import Order, Pizza, User, Ingredient

# Register your models here.

admin.site.register(Order)
admin.site.register(Pizza)
admin.site.register(User)
admin.site.register(Ingredient)
