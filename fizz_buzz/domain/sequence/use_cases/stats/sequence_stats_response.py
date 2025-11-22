from pydantic import BaseModel


class SequenceStatsResponse(BaseModel):
    most_used_request: dict | str
    hit_number: int
