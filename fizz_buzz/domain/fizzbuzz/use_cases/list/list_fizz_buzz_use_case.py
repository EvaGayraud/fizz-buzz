import json

from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_request import ListFizzBuzzRequest
from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_response import ListFizzBuzzResponse
from fizz_buzz.domain.fizzbuzz.use_cases.list.services.list_fizz_buzz_request_validation import (
    ListFizzBuzzRequestValidation,
)
from fizz_buzz.domain.fizzbuzz.use_cases.list.services.listing_fizz_buzz_use_case import ListingFizzBuzzUseCase
from fizz_buzz.domain.fizzbuzz.use_cases.list.services.logs_repository import LogsRepository


class ListFizzBuzzUseCase(ListingFizzBuzzUseCase):
    def __init__(self, validator: ListFizzBuzzRequestValidation, logs_repository: LogsRepository) -> None:
        self._validator = validator
        self._logs_repository = logs_repository

    def execute(self, request: ListFizzBuzzRequest) -> ListFizzBuzzResponse:
        self._validator.validate(request)

        request_key = json.dumps(request.to_dict(), sort_keys=True)
        self._logs_repository.record_request(request_key)

        result = []
        for i in range(1, request.limit + 1):
            entry = ""
            if i % request.integer_1 == 0:
                entry += request.string_1
            if i % request.integer_2 == 0:
                entry += request.string_2
            if not entry:
                entry = str(i)
            result.append(entry)

        return ListFizzBuzzResponse(fizz_buzz_list=result)
