from abc import ABC, abstractmethod

from fizz_buzz.domain.sequence.use_cases.list.list_fizz_buzz_request import ListFizzBuzzRequest


class ListFizzBuzzRequestValidation(ABC):
    @abstractmethod
    def validate(self, request: ListFizzBuzzRequest) -> None:
        pass
