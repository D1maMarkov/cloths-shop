from dataclasses import dataclass


@dataclass
class Brand:
    id: int
    name: str
    viewed_name: str


@dataclass
class PaginateBrand:
    id: int
    image: str | None = None
