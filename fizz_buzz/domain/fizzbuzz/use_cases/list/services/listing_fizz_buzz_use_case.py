from abc import ABC, abstractmethod

from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_request import ListFizzBuzzRequest
from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_response import ListFizzBuzzResponse


class ListingFizzBuzzUseCase(ABC):
    @abstractmethod
    def execute(self, request: ListFizzBuzzRequest) -> ListFizzBuzzResponse:
        pass
