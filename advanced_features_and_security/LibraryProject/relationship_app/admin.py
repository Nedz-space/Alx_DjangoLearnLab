# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Library
from bookshelf.models import Book  # Import from bookshelf
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'library', 'publication_year')

def setup_groups():
    """Create groups and assign permissions"""
    editors, _ = Group.objects.get_or_create(name="Editors")
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    admins, _ = Group.objects.get_or_create(name="Admins")

    content_type = ContentType.objects.get_for_model(Book)

    # Define permissions
    can_view = Permission.objects.get(codename="can_view", content_type=content_type)
    can_create = Permission.objects.get(codename="can_create", content_type=content_type)
    can_edit = Permission.objects.get(codename="can_edit", content_type=content_type)
    can_delete = Permission.objects.get(codename="can_delete", content_type=content_type)

    # Assign permissions
    viewers.permissions.add(can_view)
    editors.permissions.add(can_view, can_create, can_edit)
    admins.permissions.add(can_view, can_create, can_edit, can_delete)

