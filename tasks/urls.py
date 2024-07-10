from django.urls import path

from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.GetTasksView.as_view(), name='get_tasks'),
    path('<int:pk>', views.GetTaskView.as_view(), name='get_task'),
    path('create', views.CreateTaskView.as_view(), name='create_task'),
    # path('<int:pk>/update', , name='update_task'),
    path('<int:pk>/take', views.TakeTaskView.as_view(), name='take_task'),
    path('<int:pk>/close', views.CloseTaskView.as_view(), name='close_task'),
]
