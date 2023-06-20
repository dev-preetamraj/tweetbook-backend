from django.urls import path
from accounts.api_views.users import RegisterUserView
from accounts.api_views.profile import UserProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('register', RegisterUserView.as_view(), name='register'),
    path('profile', UserProfileView.as_view(), name='profile'),
]