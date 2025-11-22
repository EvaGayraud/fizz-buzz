from abc import ABC, abstractmethod

from fizz_buzz.domain.value_objects.identifier import Identifier


class IdentifierGeneration(ABC):
    @abstractmethod
    def generate(self, base_string: str) -> Identifier:
        pass
