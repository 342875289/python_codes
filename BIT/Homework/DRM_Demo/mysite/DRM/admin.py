from django.contrib import admin

# Register your models here.
from .models import Book,PurchaseCase


class CaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'book','count')

admin.site.register(Book)
admin.site.register(PurchaseCase,CaseAdmin)