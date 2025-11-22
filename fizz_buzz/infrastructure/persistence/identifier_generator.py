import uuid

from fizz_buzz.domain.sequence.services.identifier_generation import IdentifierGeneration
from fizz_buzz.domain.value_objects.identifier import Identifier


class IdentifierGenerator(IdentifierGeneration):
    def generate(self, base_string: str) -> Identifier:
        return Identifier(value=str(uuid.uuid5(uuid.NAMESPACE_DNS, base_string)))
