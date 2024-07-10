from rest_framework import views, generics
from rest_framework.response import Response

from users import permissions as users_permissions

from . import mixins
from . import serializers


class GetTasksView(mixins.TaskApiViewMixin, generics.ListAPIView):
    """
    Представление для получения списка задач.
    """


class GetTaskView(mixins.TaskApiViewMixin, generics.RetrieveAPIView):
    """
    Представление для получения конкретной задачи из списка задач, доступных пользователю.
    """


class CreateTaskView(mixins.TaskApiViewMixin, generics.CreateAPIView):
    """
    Представление для создания новой задачи.
    """

    serializer_class = serializers.TaskCreateSerializer
    permission_classes = [
        users_permissions.CustomerOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(status='pending', customer=self.request.user)


class UpdateTaskView(mixins.TaskApiViewMixin, generics.UpdateAPIView):
    """
    Представление для обновления задачи.
    """

    serializer_class = serializers.TaskUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)

        self.check_update_current_task_permissions(request.user)

        self.perform_update(serializer)

        return Response(serializer.data)


class TakeTaskView(mixins.TaskApiViewMixin, views.APIView):
    """
    Представление для принятия задачи.
    """

    permission_classes = [
        users_permissions.EmployeeOnly,
    ]

    def put(self, request, **kwargs):
        return self.take_current_task(request.user)


class DeclineTaskView(mixins.TaskApiViewMixin, views.APIView):
    """
    Представление для отмены работы над задачей.
    """

    permission_classes = [
        users_permissions.EmployeeOnly,
    ]

    def put(self, request, **kwargs):
        return self.decline_current_task(request.user)


class CloseTaskView(mixins.TaskApiViewMixin, views.APIView):
    """
    Представление для закрытия задачи.
    """

    permission_classes = [
        users_permissions.AllowedUserType,
    ]

    def put(self, request, pk, **kwargs):
        return self.close_current_task(request.user)
