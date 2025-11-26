from enum import Enum


class FilterConditionOperator(str, Enum):
    BETWEEN = "BETWEEN"
    IN = "IN"
    IS_NOT_NULL = "IS NOT NULL"
    IS_NULL = "IS NULL"
    LIKE = "LIKE"
    NOT_IN = "NOT IN"
    NOT_LIKE = "NOT LIKE"
    VALUE_0 = "="
    VALUE_1 = "!="
    VALUE_2 = "<"
    VALUE_3 = ">"
    VALUE_4 = "<="
    VALUE_5 = ">="

    def __str__(self) -> str:
        return str(self.value)
