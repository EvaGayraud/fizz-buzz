import json

from fizz_buzz.domain.sequence.services.store.logs_store import LogsStore
from fizz_buzz.domain.sequence.use_cases.stats.fizz_buzz_stats_response import FizzBuzzStatsResponse
from fizz_buzz.domain.sequence.use_cases.stats.services.fizz_buzz_stats_compute_use_case import (
    FizzBuzzStatsComputeUseCase,
)


class FizzBuzzStatsUseCase(FizzBuzzStatsComputeUseCase):
    def __init__(self, logs_repository: LogsStore) -> None:
        self._logs_repository = logs_repository

    def execute(self) -> FizzBuzzStatsResponse:
        request_key, hits = self._logs_repository.get_most_common()
        if not request_key:
            return FizzBuzzStatsResponse(most_used_request="No requests recorded yet", hit_number=0)

        return FizzBuzzStatsResponse(most_used_request=json.loads(request_key), hit_number=hits)
