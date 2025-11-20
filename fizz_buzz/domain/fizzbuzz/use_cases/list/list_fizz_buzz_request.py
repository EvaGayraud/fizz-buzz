from pydantic import BaseModel


class ListFizzBuzzRequest(BaseModel):
    limit: int
    integer_1: int
    integer_2: int
    string_1: str
    string_2: str

    def to_dict(self) -> dict:
        return {
            "limit": self.limit,
            "integer_1": self.integer_1,
            "integer_2": self.integer_2,
            "string_1": self.string_1,
            "string_2": self.string_2,
        }
