from collections.abc import Mapping
from types import MappingProxyType
from typing import Final

import pydantic
from starlette import status

from via_report_generator.domain.shared.exceptions.base import (
    DomainError,
    InvalidRequest,
    NotFoundError,
)
from via_report_generator.infrastructure.exceptions.base import (
    BadCredentialsException,
    BadDecodeException,
    GeminiServiceUnavailableException,
    InfrastructureException,
    UnableCredentialsException,
)

MSG_SERVICE_UNAVAILABLE: Final[str] = "Service temporarily unavailable. Please try again later."
MSG_INTERNAL_SERVER_ERROR: Final[str] = "Internal server error."

ERROR_STATUS_MAPPING: Final[Mapping[type[Exception], int]] = MappingProxyType(
    {
        DomainError: status.HTTP_500_INTERNAL_SERVER_ERROR,
        InfrastructureException: status.HTTP_500_INTERNAL_SERVER_ERROR,
        NotFoundError: status.HTTP_404_NOT_FOUND,
        pydantic.ValidationError: status.HTTP_422_UNPROCESSABLE_ENTITY,
        InvalidRequest: status.HTTP_400_BAD_REQUEST,
        NotImplementedError: status.HTTP_400_BAD_REQUEST,
        ValueError: status.HTTP_422_UNPROCESSABLE_ENTITY,
        TypeError: status.HTTP_422_UNPROCESSABLE_ENTITY,
        BadCredentialsException: status.HTTP_401_UNAUTHORIZED,
        UnableCredentialsException: status.HTTP_401_UNAUTHORIZED,
        BadDecodeException: status.HTTP_400_BAD_REQUEST,
        GeminiServiceUnavailableException: status.HTTP_502_BAD_GATEWAY,
    }
)
