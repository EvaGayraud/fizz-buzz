from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from fizz_buzz.domain.sequence.services.use_cases.sequence_stats_compute_use_case import (
    SequenceStatsComputeUseCase,
)
from fizz_buzz.domain.sequence.use_cases.stats.sequence_stats_response import SequenceStatsResponse

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
@inject
def sequence_stats(
    use_case: FromDishka[SequenceStatsComputeUseCase],
) -> SequenceStatsResponse:
    response = use_case.execute()

    return response
