from enum import Enum


class Polarity(str, Enum):
    POSITIVE = "+"
    NEGATIVE = "-"


class Tag(str, Enum):
    DELETE = "delete"
    EQUAL = "equal"
    INSERT = "insert"
    REPLACE = "replace"
