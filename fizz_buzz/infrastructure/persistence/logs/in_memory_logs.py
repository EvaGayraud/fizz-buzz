from collections import Counter

from fizz_buzz.domain.fizzbuzz.use_cases.list.services.logs_repository import LogsRepository


class InMemoryLogs(LogsRepository):
    def __init__(self) -> None:
        self.counter = Counter()

    def record_request(self, request_key: str) -> None:
        self.counter[request_key] += 1

    def get_most_common(self) -> tuple[str | None, int]:
        if not self.counter:
            return None, 0
        most_common_request, hits = self.counter.most_common(1)[0]
        return most_common_request, hits
