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

    title = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    status = serializers.CharField(max_length=15, read_only=True)
    creation_date = serializers.DateTimeField(read_only=True)
    change_date = serializers.DateTimeField(read_only=True)
    closing_date = serializers.DateTimeField(read_only=True)
    report = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    customer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    employee = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
        list_serializer_class = TaskListSerializer

    def to_representation(self, instance):
        return {'task': super(TaskSerializer, self).to_representation(instance)}
