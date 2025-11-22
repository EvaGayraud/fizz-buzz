from dishka import Provider, Scope, provide

from fizz_buzz.domain.sequence.use_cases.list.list_fizz_buzz_request_validator import ListFizzBuzzRequestValidator
from fizz_buzz.domain.sequence.use_cases.list.list_fizz_buzz_use_case import ListFizzBuzzUseCase
from fizz_buzz.domain.sequence.use_cases.list.services.listing_fizz_buzz_use_case import ListingFizzBuzzUseCase
from fizz_buzz.domain.sequence.use_cases.stats.fizz_buzz_stats_use_case import FizzBuzzStatsUseCase
from fizz_buzz.domain.sequence.use_cases.stats.services.fizz_buzz_stats_compute_use_case import (
    FizzBuzzStatsComputeUseCase,
)
from fizz_buzz.infrastructure.store.logs.in_memory_logs import InMemoryLogs


class ListFizzBuzzUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_use_case(self, logs_repository: InMemoryLogs) -> ListingFizzBuzzUseCase:
        return ListFizzBuzzUseCase(validator=ListFizzBuzzRequestValidator(), logs_repository=logs_repository)


class FizzBuzzStatsUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_use_case(self, logs_repository: InMemoryLogs) -> FizzBuzzStatsComputeUseCase:
        return FizzBuzzStatsUseCase(logs_repository=logs_repository)
