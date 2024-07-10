from django.db.models import Q

from users import services as user_services

from .models import Task


def get_user_tasks(user):
    """
    Получает список задач, доступных пользователю.
    """

    tasks = Task.objects.all()

    if user_services.is_user_customer(user):
        return tasks.filter(customer=user)

    if user_services.is_user_employee(user):
        return tasks.filter(Q(status='pending') | Q(employee=user))

    raise TypeError(f"User with type '{user.user_type and user.user_type.title}' cannot have access to tasks")
