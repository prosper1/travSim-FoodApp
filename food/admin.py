from django.contrib import admin
from .models import Food, Order, ExtendUser

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','day']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['food', 'user','cancelled','reason']


admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)
