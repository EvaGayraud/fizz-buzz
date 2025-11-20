from pydantic import BaseModel, Field


class ListFizzBuzzRequest(BaseModel):
    limit: int
    integer_1: int
    integer_2: int
    string_1: str
    string_2: str
