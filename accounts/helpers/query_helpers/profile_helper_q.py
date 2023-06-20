import logging
from django.contrib.auth.models import User
from ...models import Profile

# Get an instance of logger
logger = logging.getLogger('document_management')

def get_profile_q(request):
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
            'profile_picture': profile.profile_picture,
            'cover_picture': profile.cover_picture,
            'bio': profile.bio,
            'relationship_status': profile.relationship_status,
        }
    except Exception as e:
        logger.error(f'PROFILE QUERY HELPER get_profile_q: {e}')

    return data