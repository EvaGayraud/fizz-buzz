from collections import Counter

from fizz_buzz.domain.sequence.services.store.logs_store import LogsStore
from fizz_buzz.domain.value_objects.identifier import Identifier


class InMemoryLogs(LogsStore):
    def __init__(self) -> None:
        self.counter = Counter()

    def record(self, sequence_identifier: Identifier) -> None:
        self.counter[sequence_identifier.value] += 1

    def get_most_common(self) -> tuple[str | None, int]:
        if not self.counter:
            return None, 0
        most_common_request, hits = self.counter.most_common(1)[0]
        return most_common_request, hits
