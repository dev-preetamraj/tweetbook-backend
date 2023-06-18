from django.urls import path
from .api_views.users import Users, RegisterUserView
from .api_views.auth import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)

urlpatterns = [
    path('token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('register', RegisterUserView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('users', Users.as_view(), name='users'),
]