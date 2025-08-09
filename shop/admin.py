from django.contrib import admin
from .models import Products, tickets


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image', 'description', 'information', 'price')
    prepopulated_fields = {'slug':('name', )}


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'fname', 'lname', 'email')

admin.site.register(Products, ProductAdmin)
admin.site.register(tickets, TicketAdmin)