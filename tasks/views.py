from django.db.models import Q
from rest_framework import generics, permissions, exceptions

from users import services as user_services
from users import permissions as users_permissions

from .models import Task
from . import serializers


class GetTasksView(generics.ListAPIView):
    """
    Представление для получения списка задач
    """

    serializer_class = serializers.TaskSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        users_permissions.AllowedUserType,
    ]

    def get_queryset(self):
        if user_services.is_user_customer(self.request.user):
            return Task.objects.filter(customer=self.request.user)
        if user_services.is_user_employee(self.request.user):
            return Task.objects.filter(Q(status='pending') | Q(employee=self.request.user))
        raise exceptions.PermissionDenied
