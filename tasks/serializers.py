from rest_framework import serializers

from .models import Task


class TaskListSerializer(serializers.ListSerializer):
    """
    Сериализатор для списка моделей задач.
    """

    def to_representation(self, data):
        return [('tasks', super(TaskListSerializer, self).to_representation(data))]

    @property
    def data(self):
        return serializers.ReturnDict(
            super(TaskListSerializer, self).data,
            serializer=self,
        )


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели задачи.
    """

    class Meta:
        model = Task
        fields = '__all__'
        list_serializer_class = TaskListSerializer

    def to_representation(self, instance):
        return {'task': super(TaskSerializer, self).to_representation(instance)}
