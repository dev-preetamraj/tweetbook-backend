from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from accounts.apiviews.users_view import UsersView
from accounts.apiviews.users_profile_view import UsersProfileView

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('users', UsersView.as_view(), name='users'),
    path('profile', UsersProfileView.as_view(), name='users'),
]