# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Library, Book


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Book)
