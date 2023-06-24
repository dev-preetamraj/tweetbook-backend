import logging
from rest_framework.response import Response
from rest_framework import status

from tweetbook.utils import custom_exceptions as ce

from accounts.common import messages as app_msg
from tweetbook.common import messages as global_msg

from accounts.serializers import UserProfileSerializer

# Get an instance of logger
logger = logging.getLogger('accounts')

def get_user_profile_service(request):
    try:
        user = request.user
        profile = user.profile
        serializer = UserProfileSerializer(profile)
        return Response({
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': app_msg.USER_FETCHED,
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f'services.users_profile_services.get_user_profile_service: {e}')
        raise ce.InternalServerError