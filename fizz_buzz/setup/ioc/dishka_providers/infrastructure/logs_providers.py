from dishka import Provider, Scope, provide

from fizz_buzz.infrastructure.store.logs.in_memory_logs import InMemoryLogs


class InMemoryLogsProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_use_case(self) -> InMemoryLogs:
        return InMemoryLogs()
