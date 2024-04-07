from pydantic import BaseModel


class BaseDataFieldAddRequest(BaseModel):
    name: str
    viewed_name: str
