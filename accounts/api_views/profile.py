import logging
from rest_framework.views import APIView
from rest_framework.versioning import NamespaceVersioning

from tweetbook.utils import custom_exceptions as ce
from tweetbook.utils.custom_validators import CustomValidator

from tweetbook.common import (
    messages as global_msg,
    constants as global_const
)

from accounts.helpers.function_helpers.profile_helper_fn import (
    get_profile_fn
)

# Get an instance of logger
logger = logging.getLogger('accounts')

# Get an instance of Validator
c_validator = CustomValidator({}, allow_unknown = True)

class VersioningConfig(NamespaceVersioning):
    default_version = 'v1'
    allowed_versions = ['v1']
    version_param = 'version'

class UserProfileView(APIView):
    '''
        Manage User Profile
    '''
    versioning_class = VersioningConfig

    def get(self, request):
        try:
            if request.version == 'v1':
                result = get_profile_fn(request)
                return result
            
            else:
                raise ce.VersionNotSupported
        
        except ce.VersionNotSupported as vns:
            logger.error(f'UserProfileView API VIEW - GET : {vns}')
            raise

        except Exception as e:
            logger.error(f'UserProfileView API VIEW - GET : {e}')
            raise ce.InternalServerError