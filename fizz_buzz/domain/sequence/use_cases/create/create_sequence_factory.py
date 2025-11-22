from fizz_buzz.domain.sequence.entities.sequence import Sequence
from fizz_buzz.domain.sequence.services.identifier_generation import IdentifierGeneration
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request import CreateSequenceRequest
from fizz_buzz.domain.sequence.use_cases.create.services.create_sequence_creation import CreateSequenceCreation


class CreateSequenceFactory(CreateSequenceCreation):
    def __init__(self, identifier_generator: IdentifierGeneration) -> None:
        self._identifier_generator = identifier_generator

    def create(self, request: CreateSequenceRequest) -> Sequence:
        result = []
        for i in range(1, request.limit + 1):
            entry = ""
            if i % request.integer_1 == 0:
                entry += request.string_1
            if i % request.integer_2 == 0:
                entry += request.string_2
            if not entry:
                entry = str(i)
            result.append(entry)

        return Sequence(value=result, identifier=self._identifier_generator.generate(str(request)))
