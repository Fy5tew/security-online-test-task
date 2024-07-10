from rest_framework.permissions import BasePermission

from . import services


class AllowedUserType(BasePermission):
    """
    Класс, представляющий разрешение доступа для пользователей с разрешенным типом аккаунта.
    """

    def has_permission(self, request, view):
        return services.is_user_type_allowed(request.user)


class EmployeeOnly(BasePermission):
    """
    Класс, представляющий разрешение доступа только для сотрудников.
    """

    def has_permission(self, request, view):
        return services.is_user_employee(request.user)


class CustomerOnly(BasePermission):
    """
    Класс, представляющий разрешение доступа только для заказчиков.
    """

    def has_permission(self, request, view):
        return services.is_user_customer(request.user)
