import logging
from tweetbook.utils import custom_exceptions as ce
from django.conf import settings
from django.contrib.auth import get_user_model


from accounts.common import messages as app_msg
from tweetbook.common import messages as global_msg

# Get an instance of logger
logger = logging.getLogger('accounts')

UserAccount = get_user_model()


def is_email_unique_query(email):
    try:
        return not UserAccount.objects.filter(email=email).exists()
    except Exception as e:
        logger.error(f'queries.users_queries.is_email_unique_query: {e}')
        return False


def is_username_unique_query(username):
    try:
        return not UserAccount.objects.filter(username=username).exists()
    except Exception as e:
        logger.error(f'queries.users_queries.is_username_unique_query: {e}')
        return False


def register_user_query(data):
    try:
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        user = UserAccount.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return user

    except Exception as e:
        logger.error(f'queries.users_queries.register_user_query: {e}')
        return None
