from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TableQueryRequest")


@_attrs_define
class TableQueryRequest:
    """Request model for querying a Delta table.

    Note: For deterministic pagination with offset > 0, include an ORDER BY
    clause in your query. Without ORDER BY, rows may appear in different
    order across pages, causing duplicates or missing records.

        Attributes:
            query (str): SQL query to execute against the table
            limit (int | Unset): Maximum number of rows to return Default: 1000.
            offset (int | Unset): Number of rows to skip for pagination. Requires ORDER BY in query for deterministic
                results. Default: 0.
    """

    query: str
    limit: int | Unset = 1000
    offset: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        table_query_request = cls(
            query=query,
            limit=limit,
            offset=offset,
        )

        table_query_request.additional_properties = d
        return table_query_request

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
