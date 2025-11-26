from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.join_clause_join_type import JoinClauseJoinType

T = TypeVar("T", bound="JoinClause")


@_attrs_define
class JoinClause:
    """Model for JOIN clause specification.

    Attributes:
        join_type (JoinClauseJoinType): Type of JOIN operation
        database (str): Database containing the table to join
        table (str): Table to join
        on_left_column (str): Column from the left/main table for the join condition
        on_right_column (str): Column from the joined table for the join condition
    """

    join_type: JoinClauseJoinType
    database: str
    table: str
    on_left_column: str
    on_right_column: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        join_type = self.join_type.value

        database = self.database

        table = self.table

        on_left_column = self.on_left_column

        on_right_column = self.on_right_column

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "join_type": join_type,
                "database": database,
                "table": table,
                "on_left_column": on_left_column,
                "on_right_column": on_right_column,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        join_type = JoinClauseJoinType(d.pop("join_type"))

        database = d.pop("database")

        table = d.pop("table")

        on_left_column = d.pop("on_left_column")

        on_right_column = d.pop("on_right_column")

        join_clause = cls(
            join_type=join_type,
            database=database,
            table=table,
            on_left_column=on_left_column,
            on_right_column=on_right_column,
        )

        join_clause.additional_properties = d
        return join_clause

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
