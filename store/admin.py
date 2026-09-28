from django.contrib import admin
from store.models.products import Products
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# Admin panel mein models ko register karna
admin.site.register(Products, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)