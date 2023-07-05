from django.contrib import admin
from .models import Book

class UserAdmin(admin.ModelAdmin):
    emp_details = ['title','description','author','Created_at']


admin.site.register(Book,UserAdmin)