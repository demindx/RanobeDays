from rest_framework.views import exception_handler
from rest_framework.response import Response
from apps.core.utils import get_response_data
from rest_framework.exceptions import ValidationError


import logging


logger = logging.getLogger(__name__)


class AlreadyExistError(Exception):
    ...


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        logger.debug(str(exc))

        if isinstance(exc, ValidationError):
            return Response(data=get_response_data(exc.status_code, exc.detail),
                            status=exc.status_code)

        return Response(get_response_data(response.status_code, str(exc)),
                        response.status_code)

    return response
