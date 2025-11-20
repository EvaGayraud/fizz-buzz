from dishka import Provider, Scope, provide

from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_request_validator import ListFizzBuzzRequestValidator
from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_use_case import ListFizzBuzzUseCase
from fizz_buzz.domain.fizzbuzz.use_cases.list.services.listing_fizz_buzz_use_case import ListingFizzBuzzUseCase


class ListFizzBuzzUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_use_case(self) -> ListingFizzBuzzUseCase:
        return ListFizzBuzzUseCase(validator=ListFizzBuzzRequestValidator())
