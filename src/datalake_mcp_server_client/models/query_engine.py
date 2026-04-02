from enum import Enum


class QueryEngine(str, Enum):
    SPARK = "spark"
    TRINO = "trino"

    def __str__(self) -> str:
        return str(self.value)
