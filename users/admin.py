from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import UserType, User


class UserAdmin(DefaultUserAdmin):
    """
    Модель для представления пользователя в админ-панели Django
    """

    model = User
    list_display = ('phone', 'email', 'first_name', 'last_name', 'patronymic', 'is_staff')
    search_fields = ('phone', 'email', 'first_name', 'last_name', 'patronymic')
    ordering = ('phone',)

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'patronymic', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2')}
        ),
    )


admin.site.register(UserType)
admin.site.register(User, UserAdmin)
