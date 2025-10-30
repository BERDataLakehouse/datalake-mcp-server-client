from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TableListRequest")


@_attrs_define
class TableListRequest:
    """Request model for listing tables in a database.

    Attributes:
        database (str): Name of the database to list tables from
        use_hms (bool | Unset): Whether to use Hive Metastore client for faster metadata retrieval Default: True.
    """

    database: str
    use_hms: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database = self.database

        use_hms = self.use_hms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database": database,
            }
        )
        if use_hms is not UNSET:
            field_dict["use_hms"] = use_hms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database = d.pop("database")

        use_hms = d.pop("use_hms", UNSET)

        table_list_request = cls(
            database=database,
            use_hms=use_hms,
        )

        table_list_request.additional_properties = d
        return table_list_request

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
