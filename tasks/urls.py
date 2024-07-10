from django.urls import path

from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.GetTasksView.as_view(), name='get_tasks'),
    # path('<int:pk>', , name='get_task'),
    # path('create', , name='create_task'),
    # path('<int:pk>/update', , name='update_task'),
    # path('<int:pk>/take', , name='take_task'),
    # path('<int:pk>/close', , name='close_task'),
]
