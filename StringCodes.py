from enum import Enum

#Used for communicating operation result
class StringCodes(Enum):
    OVERFLOW = -1
    NOT_PRESENT = -2
    SUCCESS = -3
    INVALID_INPUT = -4