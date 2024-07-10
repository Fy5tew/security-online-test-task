from django.conf import settings


def is_user_type_allowed(user) -> bool:
    """
    Проверяет, является ли тип пользователя user разрешенным.
    """

    if not user.user_type:
        return False

    return user.user_type.title in settings.ALLOWED_USER_TYPES.values()


def is_user_employee(user) -> bool:
    """
    Проверяет, является ли пользователь user сотрудником.
    """

    if not user.user_type:
        return False

    return user.user_type.title == settings.ALLOWED_USER_TYPES['EMPLOYEE_TYPE_NAME']


def is_user_customer(user) -> bool:
    """
    Проверяет, является ли пользователь user заказчиком.
    """

    if not user.user_type:
        return False

    return user.user_type.title == settings.ALLOWED_USER_TYPES['CUSTOMER_TYPE_NAME']
