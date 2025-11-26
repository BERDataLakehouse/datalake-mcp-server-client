from enum import Enum


class JoinClauseJoinType(str, Enum):
    FULL = "FULL"
    INNER = "INNER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __str__(self) -> str:
        return str(self.value)
