from enum import Enum


class Size(str, Enum):
    s39 = "39 EU"
    s40 = "40 EU"
    s415 = "41.5 EU"
    s42 = "42 EU"
    s445 = "44.5 EU"
    s45 = "45 EU"
    s455 = "45.5 EU"
    s47 = "47 EU"


class BasicCategory(str, Enum):
    cloths = "cloths"
    accessories = "accessories"


class Gender(str, Enum):
    male = "male"
    female = "female"
    unisex = "unisex"


# order_status = ["В пути", "Готов к выдаче", "На складе"]
