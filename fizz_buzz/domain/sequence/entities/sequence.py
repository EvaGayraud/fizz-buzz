from pydantic import BaseModel

from fizz_buzz.domain.value_objects.identifier import Identifier


class Sequence(BaseModel):
    identifier: Identifier
    value: list
