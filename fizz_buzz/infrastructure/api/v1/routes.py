from fastapi import APIRouter

from fizz_buzz.infrastructure.api.v1.fizz_buzz import list_fizz_buzz

router = APIRouter()

router.include_router(list_fizz_buzz.router, tags=["fizz_buzzs"], prefix="/fizz_buzzs")