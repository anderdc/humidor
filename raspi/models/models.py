from pydantic import BaseModel


class SHT30X(BaseModel):
    temperature: int
    humidity: int
    # ex of an optional attribute
    # age: Optional[int] = None