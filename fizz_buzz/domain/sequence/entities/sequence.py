from pydantic import BaseModel

from fizz_buzz.domain.sequence.value_objects.identifier import Identifier


class Sequence(BaseModel):
    identifier: Identifier
    value: list
