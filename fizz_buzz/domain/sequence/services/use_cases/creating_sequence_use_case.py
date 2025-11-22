from abc import ABC, abstractmethod

from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request import CreateSequenceRequest
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_response import CreateSequenceResponse


class CreatingSequenceUseCase(ABC):
    @abstractmethod
    def execute(self, request: CreateSequenceRequest) -> CreateSequenceResponse:
        pass
