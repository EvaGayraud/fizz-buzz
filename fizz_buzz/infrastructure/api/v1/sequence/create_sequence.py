from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Body
from starlette import status

from fizz_buzz.domain.sequence.services.use_cases.creating_sequence_use_case import CreatingSequenceUseCase
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_request import CreateSequenceRequest
from fizz_buzz.domain.sequence.use_cases.create.create_sequence_response import CreateSequenceResponse

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
@inject
def create_sequence(
    use_case: FromDishka[CreatingSequenceUseCase],
    request: CreateSequenceRequest = Body(),
) -> CreateSequenceResponse:
    response = use_case.execute(request=request)

    return response
