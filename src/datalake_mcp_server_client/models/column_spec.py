from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColumnSpec")


@_attrs_define
class ColumnSpec:
    """Model for column specification in SELECT clause.

    Attributes:
        column (str): Column name to select
        table_alias (None | str | Unset): Table alias for disambiguation in JOINs
        alias (None | str | Unset): Output alias for the column (AS clause)
    """

    column: str
    table_alias: None | str | Unset = UNSET
    alias: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column = self.column

        table_alias: None | str | Unset
        if isinstance(self.table_alias, Unset):
            table_alias = UNSET
        else:
            table_alias = self.table_alias

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column": column,
            }
        )
        if table_alias is not UNSET:
            field_dict["table_alias"] = table_alias
        if alias is not UNSET:
            field_dict["alias"] = alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column = d.pop("column")

        def _parse_table_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        table_alias = _parse_table_alias(d.pop("table_alias", UNSET))

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        column_spec = cls(
            column=column,
            table_alias=table_alias,
            alias=alias,
        )

        column_spec.additional_properties = d
        return column_spec

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
