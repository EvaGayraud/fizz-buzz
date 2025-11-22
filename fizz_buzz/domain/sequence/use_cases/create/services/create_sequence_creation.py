from abc import ABC, abstractmethod

from fizz_buzz.domain.sequence.entities.sequence import Sequence
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request import CreateSequenceRequest


class CreateSequenceCreation(ABC):
    @abstractmethod
    def create(self, request: CreateSequenceRequest) -> Sequence:
        pass
