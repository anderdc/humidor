from pydantic import BaseModel


class SHT30X(BaseModel):
    temperature: float
    humidity: float
    # ex of an optional attribute
    # age: Optional[int] = None