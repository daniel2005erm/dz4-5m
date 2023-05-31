from django.contrib import admin

from apps.products.models import Products, Currency , Contact , OSP
# Register your models here.

class ProductsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

class ContactFilterAdmin(admin.ModelAdmin):
    list_filter = ('first_name', )
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

admin.site.register(Products, ProductsFilterAdmin)
admin.site.register(Contact, ContactFilterAdmin)
admin.site.register(Currency)
admin.site.register(OSP)