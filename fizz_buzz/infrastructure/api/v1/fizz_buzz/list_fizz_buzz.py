from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Body
from starlette import status

from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_request import ListFizzBuzzRequest
from fizz_buzz.domain.fizzbuzz.use_cases.list.list_fizz_buzz_response import ListFizzBuzzResponse
from fizz_buzz.domain.fizzbuzz.use_cases.list.services.listing_fizz_buzz_use_case import ListingFizzBuzzUseCase

router = APIRouter()


@router.post("", status_code=status.HTTP_200_OK)
@inject
def list_fizz_buzz(
    use_case: FromDishka[ListingFizzBuzzUseCase],
    request: ListFizzBuzzRequest = Body(),
) -> ListFizzBuzzResponse:
    response = use_case.execute(request=request)

    return response
