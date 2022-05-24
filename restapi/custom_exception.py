from rest_framework.exceptions import APIException
from rest_framework import status

class UnauthorizedUserException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Not Found"
    default_code = "Records unavailable"
