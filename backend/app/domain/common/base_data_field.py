from dataclasses import dataclass


@dataclass
class BaseDataFieldAdd:
    name: str
    viewed_name: str


@dataclass
class BaseDataField(BaseDataFieldAdd):
    id: int
