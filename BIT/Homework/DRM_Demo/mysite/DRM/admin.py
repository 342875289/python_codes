from django.contrib import admin

# Register your models here.
from .models import Book,PurchaseCase,GiftCode

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'key','ebook')

class CaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'book','count')

class CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'book')


admin.site.register(GiftCode,CodeAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(PurchaseCase,CaseAdmin)