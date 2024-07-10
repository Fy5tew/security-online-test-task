from rest_framework import generics, permissions, exceptions

from users import permissions as users_permissions

from . import services
from . import serializers


class GetTasksView(generics.ListAPIView):
    """
    Представление для получения списка задач.
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


class GetTaskView(generics.RetrieveAPIView):
    """
    Представление для получения конкретной задачи из списка задач, доступных пользователю.
    """

    serializer_class = serializers.TaskSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        users_permissions.AllowedUserType,
    ]

    def get_queryset(self):
        try:
            return (
                services.get_user_tasks(self.request.user)
                .filter(id=self.kwargs['pk'])
            )
        except TypeError:
            raise exceptions.PermissionDenied


class CreateTaskView(generics.CreateAPIView):
    """
    Представление для создания новой задачи.
    """

    serializer_class = serializers.TaskSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        users_permissions.CustomerOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(status='pending', customer=self.request.user)
