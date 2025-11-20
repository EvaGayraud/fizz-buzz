import json

from fizz_buzz.domain.fizzbuzz.use_cases.list.services.logs_repository import LogsRepository
from fizz_buzz.domain.fizzbuzz.use_cases.stats.fizz_buzz_stats_response import FizzBuzzStatsResponse
from fizz_buzz.domain.fizzbuzz.use_cases.stats.services.fizz_buzz_stats_compute_use_case import (
    FizzBuzzStatsComputeUseCase,
)


class FizzBuzzStatsUseCase(FizzBuzzStatsComputeUseCase):
    def __init__(self, logs_repository: LogsRepository) -> None:
        self._logs_repository = logs_repository

    def execute(self) -> FizzBuzzStatsResponse:
        request_key, hits = self._logs_repository.get_most_common()
        if not request_key:
            return FizzBuzzStatsResponse(most_used_request="No requests recorded yet", hit_number=0)

        return FizzBuzzStatsResponse(most_used_request=json.loads(request_key), hit_number=hits)
