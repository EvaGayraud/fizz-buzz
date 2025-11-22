from pydantic import BaseModel

from fizz_buzz.domain.sequence.entities.sequence import Sequence


class CreateSequenceResponse(BaseModel):
    sequence: Sequence
