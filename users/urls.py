from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from . import views


app_name = 'users'

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path('token/verify', TokenVerifyView.as_view(), name='verify_token'),

    path('current', views.CurrentUserView.as_view(), name='get_current_user')
]
