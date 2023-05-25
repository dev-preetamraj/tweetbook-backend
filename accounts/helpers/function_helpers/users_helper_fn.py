import logging
from rest_framework.response import Response
from rest_framework import status

from tweetbook.utils import custom_exceptions as ce

from accounts.common import messages as app_msg
from tweetbook.common import messages as global_msg

from accounts.helpers.query_helpers.users_helper_q import (
    get_user_by_email,
    get_user_by_username,
    register_user as register_user_to_db
)

# Get an instance of logger
logger = logging.getLogger('accounts')

def register_user(request):
    '''
        Register User in Database
    '''
    try:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if get_user_by_username(username) is not None:
            return Response({
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': app_msg.USERNAME_EXISTS,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if get_user_by_email(email) is not None:
            return Response({
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': app_msg.EMAIL_EXISTS,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if password != confirm_password:
            return Response({
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': app_msg.PASSWORD_MISMATCH,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = register_user_to_db(request.data)
        if user is not None:
            return Response({
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'message': app_msg.USER_CREATED,
                'data': {
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response({
                'success': False,
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': global_msg.INTERNAL_SERVER_ERROR,
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.error(f'USERS FUNCTION HELPER - register_user: {e}')
        raise ce.InternalServerError