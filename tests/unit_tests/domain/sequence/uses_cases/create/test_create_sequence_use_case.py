from unittest.mock import Mock

from support.builders.sequence_builder import SequenceBuilder

from fizz_buzz.domain.sequence.services.store.logs_store import LogsStore
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request import CreateSequenceRequest
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_use_case import CreateSequenceUseCase
from fizz_buzz.domain.sequence.use_cases.create.services.create_sequence_creation import CreateSequenceCreation
from fizz_buzz.domain.sequence.use_cases.create.services.create_sequence_request_validation import (
    CreateSequenceRequestValidation,
)


def test_that_create_sequence_use_case_successful() -> None:
    # Given
    given_request = CreateSequenceRequest(limit=10, integer_1=3, string_1="fizz", string_2="buzz", integer_2=5)
    sut = CreateSequenceUseCase(
        validator=Mock(spec=CreateSequenceRequestValidation),
        logs_repository=Mock(spec=LogsStore),
        factory=Mock(spec=CreateSequenceCreation),
    )
    sut._logs_repository.record_request.return_value = None
    sut._validator.validate.return_value = None
    sut._factory.create.return_value = SequenceBuilder().build()

    # When
    response = sut.execute(given_request)

    # Then
    assert response.sequence.value[0:5] == [1, 2, "fizz", 4, "buzz"]
    assert len(response.sequence.value) == 10
