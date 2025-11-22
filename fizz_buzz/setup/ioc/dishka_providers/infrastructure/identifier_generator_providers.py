from dishka import Provider, Scope, provide

from fizz_buzz.infrastructure.persistence.identifier_generator import IdentifierGenerator


class IdentifierGeneratorProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_generator(self) -> IdentifierGenerator:
        return IdentifierGenerator()
