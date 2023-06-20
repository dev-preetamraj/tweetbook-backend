import logging
from rest_framework.views import APIView
from rest_framework.versioning import NamespaceVersioning
from rest_framework.permissions import AllowAny

from tweetbook.utils import custom_exceptions as ce
from tweetbook.utils.custom_validators import CustomValidator

from tweetbook.common import (
    messages as global_msg,
    constants as global_const
)

from accounts.helpers.function_helpers.users_helper_fn import (
    register_user_fn
)

# Get an instance of logger
logger = logging.getLogger('accounts')

# Get an instance of Validator
c_validator = CustomValidator({}, allow_unknown = True)

class VersioningConfig(NamespaceVersioning):
    default_version = 'v1'
    allowed_versions = ['v1']
    version_param = 'version'

class RegisterUserView(APIView):
    '''
        Manage User Registration
    '''

    versioning_class = VersioningConfig
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            if request.version == 'v1':
                schema = {
                    'username': {
                        'required': True,
                        'empty': False,
                        'type': 'string'
                    },
                    'email': {
                        'required': True,
                        'empty': False,
                        'type': 'string',
                        'isemail': True
                    },
                    'first_name': {
                        'required': True,
                        'empty': False,
                        'type': 'string'
                    },
                    'last_name': {
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
                    },
                }
                is_valid = c_validator.validate(request.data, schema)
                if is_valid:
                    result = register_user_fn(request)
                    return result
                else:
                    raise ce.ValidationFailed({
                        'message': global_msg.VALIDATION_FAILED,
                        'data': c_validator.errors
                    })
            else:
                raise ce.VersionNotSupported
            
        except ce.ValidationFailed as vf:
            logger.error(f'RegisterUserView API VIEW - POST : {vf}')
            raise

        except ce.VersionNotSupported as vns:
            logger.error(f'RegisterUserView API VIEW - POST : {vns}')
            raise

        except Exception as e:
            logger.error(f'RegisterUserView API VIEW - POST : {e}')
            raise ce.InternalServerError
