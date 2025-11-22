from fizz_buzz.domain.sequence.entities.sequence import Sequence
from fizz_buzz.domain.value_objects.identifier import Identifier


class SequenceBuilder:
    def __init__(self) -> None:
        self._identifier = Identifier(value="1KOJHUUIOP")
        self._value = [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz"]

    def build(self) -> Sequence:
        return Sequence(identifier=self._identifier, value=self._value)
