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

from accounts.services.users_services import (
    register_user_service
)

# Get an instance of logger
logger = logging.getLogger('accounts')

# Get an instance of Validator
c_validator = CustomValidator({}, allow_unknown = True)

class VersioningConfig(NamespaceVersioning):
    default_version = 'v1'
    allowed_versions = ['v1']
    version_param = 'version'

class UsersView(APIView):
    '''
    Handle Users Registration and User Related Stuff
    '''

    versioning_class = VersioningConfig
    permission_classes = [AllowAny]

    def post(self, request):
        '''
        [summary]:
            Args:
            request (POST):
            email: Unique email address for registration
            username: Unique username
            password: 8 or more character long string
            confirm_password: Password for confirmation
        Returns:
            json: created user object
        '''

        try:
            if request.version == 'v1':
                schema = {
                    'email': {
                        'required': True,
                        'empty': False,
                        'type': 'string',
                        'isemail': True
                    },
                    'username': {
                        'required': True,
                        'empty': False,
                        'type': 'string'
                    },
                    'password': {
                        'required': True,
                        'empty': False,
                        'type': 'string',
                        'minlength': 8
                    },
                    'confirm_password': {
                        'required': True,
                        'empty': False,
                        'type': 'string',
                        'minlength': 8
                    }
                }

                is_valid = c_validator.validate(request.data, schema)
                if is_valid:
                    result = register_user_service(request)
                    return result
                else:
                    raise ce.ValidationFailed({
                        'message': global_msg.VALIDATION_FAILED,
                        'data': c_validator.errors
                    })

            else:
                raise ce.VersionNotSupported
        
        except ce.ValidationFailed as vf:
            logger.error(f'UsersView - post : {vf}')
            raise

        except ce.VersionNotSupported as vns:
            logger.error(f'UsersView - post : {vns}')
            raise

        except Exception as e:
            logger.error(f'UsersView - post : {e}')
            raise ce.InternalServerError