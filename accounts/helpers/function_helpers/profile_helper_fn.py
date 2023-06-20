import logging
from rest_framework.response import Response
from rest_framework import status

from tweetbook.utils import custom_exceptions as ce

from accounts.common import messages as app_msg
from tweetbook.common import messages as global_msg

from accounts.helpers.query_helpers.profile_helper_q import (
    get_profile_q
)

# Get an instance of logger
logger = logging.getLogger('accounts')

def get_profile_fn(request):
    '''
        Function Helper for Retrieving User Profile
    '''
    try:
        profile = get_profile_q(request)
        return Response({
            'success': True,
            'status_code': status.HTTP_201_CREATED,
            'message': app_msg.PROFILE_FETCHED,
            'data': profile
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        logger.error(f'PROFILE FUNCTION HELPER - get_profile_fn: {e}')
        raise ce.InternalServerError