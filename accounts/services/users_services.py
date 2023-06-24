import logging
from rest_framework.response import Response
from rest_framework import status

from tweetbook.utils import custom_exceptions as ce

from accounts.common import messages as app_msg
from tweetbook.common import messages as global_msg

from accounts.queries.users_queries import (
    is_email_unique_query,
    is_username_unique_query,
    register_user_query
)

from accounts.serializers import (
    UserAccountSerializer
)

# Get an instance of logger
logger = logging.getLogger('accounts')

def register_user_service(request):
    try:
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if not is_email_unique_query(email):
            return Response({
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': app_msg.EMAIL_EXISTS,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if not is_username_unique_query(username):
            return Response({
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': app_msg.USERNAME_EXISTS,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if password != confirm_password:
            return Response({
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': app_msg.PASSWORD_MISMATCH,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = register_user_query(request.data)
        serializer = UserAccountSerializer(user)
        return Response({
            'success': True,
            'status_code': status.HTTP_201_CREATED,
            'message': app_msg.USER_CREATED,
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        logger.error(f'services.users_services.register_user_service: {e}')
        raise ce.InternalServerError