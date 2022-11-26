from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, SocialLink


# Register your models here.
@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {
        "fields": (
            'role',
            'is_deleted',
        )
    }),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {
        "fields": (
            'role',
            'is_deleted',
        )
    }),)
    list_display = (
        'id',
        'username',
        'role',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
    )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'link')
