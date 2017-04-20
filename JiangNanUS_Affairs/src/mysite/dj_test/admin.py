from django.contrib import admin

# Register your models here.
from .models import Person
# Register your models here.
'''
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
'''

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
       # (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['first_name'], 'classes': ['last_name']}),
    ]
  #  inlines = [ChoiceInline]
    list_display = ('first_name', 'last_name')
    #search_fields = ['question_text']
admin.site.register(Person, PersonAdmin)
