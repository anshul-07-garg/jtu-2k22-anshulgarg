from rest_framework.exceptions import APIException
from enum import Enum, unique


@unique
class HttpStatusCode(Enum):
    """ 
    HttpStatusCode Enum

    Example usage:
        HttpStatusCode.OK.value  # 100
        HttpStatusCode.INTERNAL_SERVER_ERROR.value  # 500
    """
    BAD_REQUEST = 400


class UnauthorizedUserException(APIException):
    status_code = HttpStatusCode.BAD_REQUEST.value
    default_detail = "Not Found"
    default_code = "Records unavailable"