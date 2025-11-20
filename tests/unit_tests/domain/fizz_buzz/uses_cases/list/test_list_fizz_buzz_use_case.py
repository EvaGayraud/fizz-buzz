from unittest.mock import Mock

from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_request import ListFizzBuzzRequest
from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_use_case import ListFizzBuzzUseCase
from fizz_buzz.domain.fizzbuzz.use_cases.list.services.list_fizz_buzz_request_validation import \
    ListFizzBuzzRequestValidation


def test_that_list_fizz_buzz_use_case_successful() -> None:
    # Given
    given_request = ListFizzBuzzRequest(limit=100, integer_1=3, string_1="fizz", string_2="buzz", integer_2=5)
    sut = ListFizzBuzzUseCase(validator=Mock(spec=ListFizzBuzzRequestValidation))
    sut._validator.validate.return_value = None

    # When
    response = sut.execute(given_request)

    # Then
    assert response.fizz_buzz_list[0:5] == ["1", "2", "fizz", "4", "buzz"]
    assert response.fizz_buzz_list[14] == "fizzbuzz"
    assert len(response.fizz_buzz_list) == 100
