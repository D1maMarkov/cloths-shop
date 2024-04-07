from pydantic import BaseModel


class SearchProductsRequest(BaseModel):
    search: str
