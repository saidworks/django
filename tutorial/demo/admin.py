
from django.contrib import admin
from .models import Book,ISBN,Character


""" we can edit the administration menu of django , some examples:
    -if I do not need some of the fields I can use the decorator @admin.register(Model_name) then  define a class admin.ModelAdmin 
    -fiels: a property inside the class we can assign it to a list that contains the fields I want to display
    -list_display: a property to edit how display the list of entries on the administration 
"""
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields =["title","price",'description','is_published','published','ISBN','character']
    list_display = ['title','description','price']
    list_filter = ['published'] # filter by
    search_fields = ['title'] # search option

admin.site.register(ISBN)

admin.site.register(Character)