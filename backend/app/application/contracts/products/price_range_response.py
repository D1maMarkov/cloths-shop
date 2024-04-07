from pydantic import BaseModel


class PriceRangeResponse(BaseModel):
    min_price: int
    max_price: int
