from abc import ABC, abstractmethod

from fizz_buzz.domain.fizzbuzz.use_cases.stats.fizz_buzz_stats_response import FizzBuzzStatsResponse


class FizzBuzzStatsComputeUseCase(ABC):
    @abstractmethod
    def execute(self) -> FizzBuzzStatsResponse:
        pass
