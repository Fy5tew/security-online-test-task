from rest_framework import views, permissions, generics

from . import serializers


class CurrentUserView(generics.RetrieveAPIView):
    """
    Представление для получения информации о текущем (авторизованном) пользователе.
    """

    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
