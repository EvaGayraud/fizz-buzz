from abc import ABC, abstractmethod

from fizz_buzz.domain.sequence.use_cases.stats.sequence_stats_response import SequenceStatsResponse


class SequenceStatsComputeUseCase(ABC):
    @abstractmethod
    def execute(self) -> SequenceStatsResponse:
        pass
