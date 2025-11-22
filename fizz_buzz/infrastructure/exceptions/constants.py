from collections.abc import Mapping
from types import MappingProxyType
from typing import Final

import pydantic
from starlette import status

from fizz_buzz.domain.sequence.exceptions.base import InvalidRequest

MSG_SERVICE_UNAVAILABLE: Final[str] = "Service temporarily unavailable. Please try again later."
MSG_INTERNAL_SERVER_ERROR: Final[str] = "Internal server error."

ERROR_STATUS_MAPPING: Final[Mapping[type[Exception], int]] = MappingProxyType(
    {
        pydantic.ValidationError: status.HTTP_422_UNPROCESSABLE_ENTITY,
        InvalidRequest: status.HTTP_400_BAD_REQUEST,
        NotImplementedError: status.HTTP_400_BAD_REQUEST,
        ValueError: status.HTTP_422_UNPROCESSABLE_ENTITY,
        TypeError: status.HTTP_422_UNPROCESSABLE_ENTITY,
    }
)
