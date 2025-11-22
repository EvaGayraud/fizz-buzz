from dishka import Provider, Scope, provide

from fizz_buzz.domain.sequence.services.use_cases.creating_sequence_use_case import CreatingSequenceUseCase
from fizz_buzz.domain.sequence.services.use_cases.sequence_stats_compute_use_case import (
    SequenceStatsComputeUseCase,
)
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_factory import CreateSequenceFactory
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request_validator import CreateSequenceRequestValidator
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_use_case import CreateSequenceUseCase
from fizz_buzz.domain.sequence.use_cases.stats.sequence_stats_use_case import SequenceStatsUseCase
from fizz_buzz.infrastructure.persistence.identifier_generator import IdentifierGenerator
from fizz_buzz.infrastructure.persistence.logs.in_memory_logs import InMemoryLogs


class ListFizzBuzzUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_factory(self, identifier_generator: IdentifierGenerator) -> CreateSequenceFactory:
        return CreateSequenceFactory(identifier_generator=identifier_generator)

    @provide(scope=Scope.REQUEST)
    def provide_use_case(
        self, logs_repository: InMemoryLogs, factory: CreateSequenceFactory
    ) -> CreatingSequenceUseCase:
        return CreateSequenceUseCase(
            validator=CreateSequenceRequestValidator(), logs_repository=logs_repository, factory=factory
        )


class FizzBuzzStatsUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_use_case(self, logs_repository: InMemoryLogs) -> SequenceStatsComputeUseCase:
        return SequenceStatsUseCase(logs_repository=logs_repository)
