import pytest

from fizz_buzz.domain.sequence.exceptions.base import InvalidRequest
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request import CreateSequenceRequest
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request_validator import CreateSequenceRequestValidator


def test_that_list_sequence_request_validator_with_invalid_request_raises_exception() -> None:
    # Given
    given_request = CreateSequenceRequest(limit=0, integer_1=0, string_1="", string_2="", integer_2=0)
    sut = CreateSequenceRequestValidator()

    # When Then
    with pytest.raises(InvalidRequest):
        sut.validate(given_request)


def test_that_list_sequence_request_validator_with_valid_request_successful() -> None:
    # Given
    given_request = CreateSequenceRequest(limit=19, integer_1=5, string_1="t", string_2="u", integer_2=9)
    sut = CreateSequenceRequestValidator()

    # When Then
    sut.validate(given_request)
