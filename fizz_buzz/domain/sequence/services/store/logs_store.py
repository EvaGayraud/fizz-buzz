from abc import ABC, abstractmethod


class LogsStore(ABC):
    @abstractmethod
    def record_request(self, request_key: str) -> None:
        pass

    @abstractmethod
    def get_most_common(self) -> tuple[str | None, int]:
        pass
