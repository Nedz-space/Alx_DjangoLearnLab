#Admin.py
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, Author, Library, CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Ensure publication_year exists
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author__name')  # Fix for ForeignKey

class CustomUserAdmin(UserAdmin):
    """Admin customization for CustomUser."""
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'date_of_birth')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_superuser'),
        }),
    )
    ordering = ('email',)



def setup_groups():
    """Create user groups and assign permissions"""
    
    # Define group names
    groups_permissions = {
        "Viewers": ["can_view"],
        "Editors": ["can_edit", "can_create"],
        "Admins": ["can_edit", "can_create", "can_delete"]
    }

    # Get content type for Book model
    book_content_type = ContentType.objects.get_for_model(Book)

    for group_name, perm_names in groups_permissions.items():
        # Get or create group
        group, created = Group.objects.get_or_create(name=group_name)
        
        for perm_codename in perm_names:
            permission, _ = Permission.objects.get_or_create(
                codename=perm_codename,
                content_type=book_content_type,
                defaults={"name": f"Can {perm_codename.replace('_', ' ')} book"}
            )
            group.permissions.add(permission)
    
    print("Groups and permissions have been set up successfully.")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Library)

