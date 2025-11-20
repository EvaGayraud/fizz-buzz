from pydantic import BaseModel


class ListFizzBuzzResponse(BaseModel):
    fizz_buzz_list: list
