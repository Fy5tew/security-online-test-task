from rest_framework import views, permissions, exceptions
from rest_framework.response import Response

from users import permissions as users_permissions

from . import services
from . import serializers


class TaskApiViewMixin:
    """
    Миксин с основными полями для работы представлений заданий.
    """

    serializer_class = serializers.TaskSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        users_permissions.AllowedUserType,
    ]

    def get_queryset(self):
        try:
            return services.get_user_tasks(self.request.user)
        except TypeError:
            raise exceptions.PermissionDenied

    def get_current_task(self):
        """
        Возвращает текущую задачу (по маршруту запроса).
        """

        task = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if not task:
            raise exceptions.NotFound
        return task

    def take_current_task(self, user):
        """
        Принимает текущую задачу от пользователя user.
        """

        return self._make_action_with_current_task(
            action=services.take_task,
            user=user,
        )

    def decline_current_task(self, user):
        """
        Отменяет работу над задачей для текущего пользователя user.
        """

        return self._make_action_with_current_task(
            action=services.decline_task,
            user=user,
        )

    def close_current_task(self, user):
        """
        Закрывает текущую задачу от пользователя user.
        """

        return self._make_action_with_current_task(
            action=services.close_task,
            user=user,
        )

    def check_update_current_task_permissions(self, user):
        """
        Проверяет, может ли пользователь обновлять текущую задачу.
        """

        try:
            task = self.get_current_task()
            services.check_edit_task_permissions(task=task, user=user)
        except (TypeError, ValueError) as ex:
            raise exceptions.PermissionDenied(ex)

    def _make_action_with_current_task(self, action, user):
        """
        Производит действие action для текущей задачи от пользователя user.
        """

        try:
            task = self.get_current_task()
            action(task, user)
            return Response(serializers.TaskSerializer(task).data)
        except (TypeError, ValueError) as ex:
            raise exceptions.PermissionDenied(ex)
