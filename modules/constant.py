from enum import Enum


class Tag(str, Enum):
    DELETE = "delete"
    EQUAL = "equal"
    INSERT = "insert"
    REPLACE = "replace"


class Polarity(str, Enum):
    POSITIVE = "+"
    NEGATIVE = "-"
