from enum import Enum


class OrderStatus(str, Enum):
    OnTheWay = "В пути"
    ReadyToBeIssued = "Готов к выдаче"
    InTheWarehouse = "На складе"
