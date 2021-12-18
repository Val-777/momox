from enum import Enum


class Status(str, Enum):
    PRESENT = "PRESENT"
    HOLD = "HOLD"
    SOLD = "SOLD"
