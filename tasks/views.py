from rest_framework import views, generics, permissions, exceptions
from rest_framework.response import Response

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


class TakeTaskView(views.APIView):
    """
    Представление для принятия задачи.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        users_permissions.EmployeeOnly,
    ]

    def get_queryset(self):
        try:
            return (
                services.get_user_tasks(self.request.user)
                .filter(id=self.kwargs['pk'])
            )
        except TypeError:
            raise exceptions.PermissionDenied

    def put(self, request, pk, **kwargs):
        try:
            task = self.get_queryset().first()
            if not task:
                raise exceptions.NotFound
            services.take_task(task, request.user)
            return Response(serializers.TaskSerializer(task).data)
        except TypeError as ex:
            raise exceptions.PermissionDenied(ex)
        except ValueError as ex:
            raise exceptions.PermissionDenied(ex)


class DeclineTaskView(views.APIView):
    """
    Представление для отмены работы над задачей.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        users_permissions.EmployeeOnly,
    ]

    def get_queryset(self):
        try:
            return (
                services.get_user_tasks(self.request.user)
                .filter(id=self.kwargs['pk'])
            )
        except TypeError:
            raise exceptions.PermissionDenied

    def put(self, request, pk, **kwargs):
        try:
            task = self.get_queryset().first()
            if not task:
                raise exceptions.NotFound
            services.decline_task(task, request.user)
            return Response(serializers.TaskSerializer(task).data)
        except TypeError as ex:
            raise exceptions.PermissionDenied(ex)
        except ValueError as ex:
            raise exceptions.PermissionDenied(ex)


class CloseTaskView(views.APIView):
    """
    Представление для закрытия задачи.
    """

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

    def put(self, request, pk, **kwargs):
        try:
            task = self.get_queryset().first()
            if not task:
                raise exceptions.NotFound
            services.close_task(task, request.user)
            return Response(serializers.TaskSerializer(task).data)
        except TypeError as ex:
            raise exceptions.PermissionDenied(ex)
        except ValueError as ex:
            raise exceptions.PermissionDenied(ex)
