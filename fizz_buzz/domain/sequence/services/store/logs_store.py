from abc import ABC, abstractmethod

from fizz_buzz.domain.value_objects.identifier import Identifier


class LogsStore(ABC):
    @abstractmethod
    def record(self, sequence_identifier: Identifier) -> None:
        pass

    @abstractmethod
    def get_most_common(self) -> tuple[str | None, int]:
        pass
