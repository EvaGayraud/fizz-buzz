import pytest

from fizz_buzz.domain.sequence.exceptions.base import InvalidRequest
from fizz_buzz.domain.sequence.use_cases.list.list_fizz_buzz_request import ListFizzBuzzRequest
from fizz_buzz.domain.sequence.use_cases.list.list_fizz_buzz_request_validator import ListFizzBuzzRequestValidator


def test_that_list_fizz_buzz_request_validator_with_invalid_request_raises_exception() -> None:
    # Given
    given_request = ListFizzBuzzRequest(limit=0, integer_1=0, string_1="", string_2="", integer_2=0)
    sut = ListFizzBuzzRequestValidator()

    # When Then
    with pytest.raises(InvalidRequest):
        sut.validate(given_request)


def test_that_list_fizz_buzz_request_validator_with_valid_request_successful() -> None:
    # Given
    given_request = ListFizzBuzzRequest(limit=19, integer_1=5, string_1="t", string_2="u", integer_2=9)
    sut = ListFizzBuzzRequestValidator()

    # When Then
    sut.validate(given_request)
