from fizz_buzz.domain.sequence.services.store.logs_store import LogsStore
from fizz_buzz.domain.sequence.services.use_cases.creating_sequence_use_case import CreatingSequenceUseCase
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request import CreateSequenceRequest
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_response import CreateSequenceResponse
from fizz_buzz.domain.sequence.use_cases.create.services.create_sequence_creation import CreateSequenceCreation
from fizz_buzz.domain.sequence.use_cases.create.services.create_sequence_request_validation import (
    CreateSequenceRequestValidation,
)


class CreateSequenceUseCase(CreatingSequenceUseCase):
    def __init__(
        self, validator: CreateSequenceRequestValidation, logs_repository: LogsStore, factory: CreateSequenceCreation
    ) -> None:
        self._validator = validator
        self._logs_repository = logs_repository
        self._factory = factory

    def execute(self, request: CreateSequenceRequest) -> CreateSequenceResponse:
        self._validator.validate(request)

        sequence = self._factory.create(request)

        self._logs_repository.record_request(sequence.identifier)

        return CreateSequenceResponse(sequence=sequence)
