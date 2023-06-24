from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from accounts.models import Profile

class UserAccountSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'username']

class UserSerializerForProfile(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'first_name', 'last_name']

class UserProfileSerializer(ModelSerializer):
    user = UserSerializerForProfile()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'dob', 'gender', 'profile_picture', 'cover_picture', 'bio', 'relationship_status']