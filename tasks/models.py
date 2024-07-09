from django.db import models
from django.utils import timezone


class Task(models.Model):
    """
    Модель, представляющая задачу для выполнения.
    """

    STATUSES = [
        ('pending', 'Pending'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed')
    ]

    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUSES, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)
    closing_date = models.DateTimeField(null=True, blank=True)
    report = models.TextField(null=True, blank=True)
    customer = models.ForeignKey('users.User', related_name='customer', on_delete=models.CASCADE, null=False, blank=False)
    employee = models.ForeignKey('users.User', related_name='employee', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
