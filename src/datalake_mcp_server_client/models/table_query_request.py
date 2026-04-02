from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.query_engine import QueryEngine
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
            limit (int | Unset): Maximum number of rows to return Default: 100.
            offset (int | Unset): Number of rows to skip for pagination. Requires ORDER BY in query for deterministic
                results. Default: 0.
            engine (None | QueryEngine | Unset): Query engine to use. Overrides the global QUERY_ENGINE setting. If not
                specified, uses the QUERY_ENGINE env var (default: spark).
    """

    query: str
    limit: int | Unset = 100
    offset: int | Unset = 0
    engine: None | QueryEngine | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        limit = self.limit

        offset = self.offset

        engine: None | str | Unset
        if isinstance(self.engine, Unset):
            engine = UNSET
        elif isinstance(self.engine, QueryEngine):
            engine = self.engine.value
        else:
            engine = self.engine

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
        if engine is not UNSET:
            field_dict["engine"] = engine

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        def _parse_engine(data: object) -> None | QueryEngine | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                engine_type_0 = QueryEngine(data)

                return engine_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QueryEngine | Unset, data)

        engine = _parse_engine(d.pop("engine", UNSET))

        table_query_request = cls(
            query=query,
            limit=limit,
            offset=offset,
            engine=engine,
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
