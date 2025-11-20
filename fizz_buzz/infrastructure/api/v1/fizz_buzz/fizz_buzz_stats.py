from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from fizz_buzz.domain.fizzbuzz.use_cases.stats.fizz_buzz_stats_response import FizzBuzzStatsResponse
from fizz_buzz.domain.fizzbuzz.use_cases.stats.services.fizz_buzz_stats_compute_use_case import (
    FizzBuzzStatsComputeUseCase,
)

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
@inject
def fizz_buzz_stats(
    use_case: FromDishka[FizzBuzzStatsComputeUseCase],
) -> FizzBuzzStatsResponse:
    response = use_case.execute()

    return response
