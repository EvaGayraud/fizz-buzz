from pydantic import BaseModel


class FizzBuzzStatsResponse(BaseModel):
    most_used_request: dict | str
    hit_number: int
