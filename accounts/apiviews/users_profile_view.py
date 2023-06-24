import logging

from rest_framework.views import APIView
from rest_framework.versioning import NamespaceVersioning
from rest_framework.permissions import AllowAny

from tweetbook.utils import custom_exceptions as ce
from tweetbook.utils.custom_validators import CustomValidator

from tweetbook.common import (
    messages as global_msg
)

from accounts.common import (
    messages as app_msg
)

from accounts.services.users_profile_services import (
    get_user_profile_service
)

# Get an instance of logger
logger = logging.getLogger('accounts')

# Get an instance of Validator
c_validator = CustomValidator({}, allow_unknown = True)

class VersioningConfig(NamespaceVersioning):
    default_version = 'v1'
    allowed_versions = ['v1']
    version_param = 'version'

class UsersProfileView(APIView):
    '''
    Handle Users Registration and User Related Stuff
    '''

    versioning_class = VersioningConfig

    def get(self, request):
        '''
        [summary]:
            Args:
            request (GET):
        Returns:
            json: users profile
        '''

        try:
            if request.version == 'v1':
                result = get_user_profile_service(request)
                return result

            else:
                raise ce.VersionNotSupported
        
        except ce.ValidationFailed as vf:
            logger.error(f'UsersProfileView - get : {vf}')
            raise

        except ce.VersionNotSupported as vns:
            logger.error(f'UsersProfileView - get : {vns}')
            raise

        except Exception as e:
            logger.error(f'UsersProfileView - get : {e}')
            raise ce.InternalServerError