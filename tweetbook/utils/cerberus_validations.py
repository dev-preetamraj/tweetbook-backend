import re
from tweetbook.common import messages as global_msg

def validate_pincode(field, value, error):
    """ Test the oddity of a value.
    - , _, @, ., /, #, &, +
    The rule's arguments are validated against this schema:
    """
    if not re.match("^[1-9]{1}[0-9]{2}[0-9]{3}$", value):
        error(field, global_msg.INVALID_PINCODE)

def validate_date_format(field, value, error):
    """ Test the oddity of a value.
    - , _, @, ., /, #, &, +
    The rule's arguments are validated against this schema:
    Validating date format to DD/MM/YYYY
    """
    if not re.match(
            '^(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}$', value):
        error(field, global_msg.INVALID_DATE_FORMAT)

def validate_captcha(field, value, error):
    """ Test the oddity of a value.
    - , _, @, ., /, #, &, +
    The rule's arguments are validated against this schema:
    validating payment type upfront or emi
    """
    if not re.match(
            '^[a-zA-Z0-9]{6,}$', value):
        error(field, global_msg.INVALID_CAPTCHA_CODE)

def validate_empty_string(field, value, error):
    """ Test the oddity of a value.
    - , _, @, ., /, #, &, +
    The rule's arguments are validated against this schema:
    validating payment type upfront or emi
    """
    if not re.match(
            '^[^\s]+(\s.*)?$', value):
        error(field, global_msg.EMPTY_STRING_VALIDATION)