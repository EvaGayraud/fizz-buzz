from dishka import Provider, Scope, provide

from fizz_buzz.infrastructure.persistence.logs.in_memory_logs import InMemoryLogs


class InMemoryLogsProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_in_memory(self) -> InMemoryLogs:
        return InMemoryLogs()
