from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя системы.

    Заменяет идентификатор типа пользователя его текстовым представлением.
    """

    user_type = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'phone', 'email', 'last_name', 'first_name', 'patronymic', 'user_type']
