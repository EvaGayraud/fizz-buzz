from fizz_buzz.domain.fizzbuzz.exceptions.base import InvalidRequest
from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_request import ListFizzBuzzRequest
from fizz_buzz.domain.fizzbuzz.use_cases.list.services.list_fizz_buzz_request_validation import (
    ListFizzBuzzRequestValidation,
)


class ListFizzBuzzRequestValidator(ListFizzBuzzRequestValidation):
    def validate(self, request: ListFizzBuzzRequest) -> None:
        if request.limit == 0:
            raise InvalidRequest("Limit must be greater than 0")

        if request.integer_1 == 0 or request.integer_1 > 100:
            raise InvalidRequest("Integer 1 must be greater than 0 and less than 100")

        if request.integer_2 == 0 or request.integer_2 > 100:
            raise InvalidRequest("Integer 2 must be greater than 0 and less than 100")
