from abc import ABC, abstractmethod

from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request import CreateSequenceRequest


class CreateSequenceRequestValidation(ABC):
    @abstractmethod
    def validate(self, request: CreateSequenceRequest) -> None:
        pass
