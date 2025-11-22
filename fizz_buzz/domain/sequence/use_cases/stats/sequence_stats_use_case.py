from fizz_buzz.domain.sequence.services.store.logs_store import LogsStore
from fizz_buzz.domain.sequence.services.use_cases.sequence_stats_compute_use_case import (
    SequenceStatsComputeUseCase,
)
from fizz_buzz.domain.sequence.use_cases.stats.sequence_stats_response import SequenceStatsResponse


class SequenceStatsUseCase(SequenceStatsComputeUseCase):
    def __init__(self, logs_repository: LogsStore) -> None:
        self._logs_repository = logs_repository

    def execute(self) -> SequenceStatsResponse:
        request_identifier, hits = self._logs_repository.get_most_common()
        if not request_identifier:
            return SequenceStatsResponse(most_used_request="No requests recorded yet", hit_number=0)

        return SequenceStatsResponse(most_used_request=request_identifier, hit_number=hits)
