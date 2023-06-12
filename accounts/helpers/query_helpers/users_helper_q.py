import logging
from django.contrib.auth.models import User

# Get an instance of logger
logger = logging.getLogger('document_management')

def get_user_by_username(username):
    user = None
    try:
        user_q = User.objects.get(username=username)
        if user_q:
            user = user_q

    except Exception as e:
        logger.error(f'USERS QUERY HELPER get_user_by_username: {e}')

    return user

def get_user_by_email(email):
    user = None
    try:
        user_q = User.objects.get(email=email)
        if user_q:
            user = user_q

    except Exception as e:
        logger.error(f'USERS QUERY HELPER get_user_by_email: {e}')
        
    return user

def register_user_query(data):
    user = None
    try:
        username = data.get('username')
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.first_name = first_name
        user.last_name = last_name
        user.save()

    except Exception as e:
        logger.error(f'USERS QUERY HELPER register_user: {e}')
    
    return user

def get_user_and_profile_query(request):
    data = {}
    try:
        user = request.user
        profile = user.profile

        data['id'] = user.id
        data['username'] = user.username
        data['first_name'] = user.first_name
        data['last_name'] = user.last_name
        data['email'] = user.email
        data['profile'] = {
            'dob': profile.dob,
            'gender': profile.gender,
            'profile_picture': f'http://127.0.0.1:8000{profile.profile_picture.url}',
            'cover_picture': f'http://127.0.0.1:8000{profile.cover_picture.url}',
            'bio': profile.bio,
            'relationship_status': profile.relationship_status,
        }

    except Exception as e:
        logger.error(f'USERS QUERY HELPER get_user_and_profile: {e}')

    return data