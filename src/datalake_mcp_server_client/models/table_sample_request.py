from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TableSampleRequest")


@_attrs_define
class TableSampleRequest:
    """Request model for sampling data from a Delta table.

    Attributes:
        database (str): Name of the database containing the table
        table (str): Name of the table to sample from
        limit (int | Unset): Maximum number of rows to return in the sample Default: 10.
        columns (list[str] | None | Unset): List of columns to return in the sample
        where_clause (None | str | Unset): SQL WHERE clause to filter the rows
    """

    database: str
    table: str
    limit: int | Unset = 10
    columns: list[str] | None | Unset = UNSET
    where_clause: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database = self.database

        table = self.table

        limit = self.limit

        columns: list[str] | None | Unset
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, list):
            columns = self.columns

        else:
            columns = self.columns

        where_clause: None | str | Unset
        if isinstance(self.where_clause, Unset):
            where_clause = UNSET
        else:
            where_clause = self.where_clause

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database": database,
                "table": table,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if columns is not UNSET:
            field_dict["columns"] = columns
        if where_clause is not UNSET:
            field_dict["where_clause"] = where_clause

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database = d.pop("database")

        table = d.pop("table")

        limit = d.pop("limit", UNSET)

        def _parse_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = cast(list[str], data)

                return columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        columns = _parse_columns(d.pop("columns", UNSET))

        def _parse_where_clause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        where_clause = _parse_where_clause(d.pop("where_clause", UNSET))

        table_sample_request = cls(
            database=database,
            table=table,
            limit=limit,
            columns=columns,
            where_clause=where_clause,
        )

        table_sample_request.additional_properties = d
        return table_sample_request

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
