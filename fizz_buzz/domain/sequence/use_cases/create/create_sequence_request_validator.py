from fizz_buzz.domain.sequence.exceptions.base import InvalidRequest
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request import CreateSequenceRequest
from fizz_buzz.domain.sequence.use_cases.create.services.create_sequence_request_validation import (
    CreateSequenceRequestValidation,
)


class CreateSequenceRequestValidator(CreateSequenceRequestValidation):
    def validate(self, request: CreateSequenceRequest) -> None:
        if request.limit == 0:
            raise InvalidRequest("Limit must be greater than 0")

        if request.integer_1 == 0 or request.integer_1 > 100:
            raise InvalidRequest("Integer 1 must be greater than 0 and less than 100")

        if request.integer_2 == 0 or request.integer_2 > 100:
            raise InvalidRequest("Integer 2 must be greater than 0 and less than 100")
