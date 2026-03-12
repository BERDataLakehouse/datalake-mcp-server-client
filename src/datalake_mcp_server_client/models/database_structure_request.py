from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseStructureRequest")


@_attrs_define
class DatabaseStructureRequest:
    """Request model for getting database structure.

    Attributes:
        with_schema (bool | Unset): Whether to include table schemas in the response Default: False.
        use_hms (bool | Unset): Whether to use Hive Metastore client for faster metadata retrieval Default: True.
    """

    with_schema: bool | Unset = False
    use_hms: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        with_schema = self.with_schema

        use_hms = self.use_hms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if with_schema is not UNSET:
            field_dict["with_schema"] = with_schema
        if use_hms is not UNSET:
            field_dict["use_hms"] = use_hms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        with_schema = d.pop("with_schema", UNSET)

        use_hms = d.pop("use_hms", UNSET)

        database_structure_request = cls(
            with_schema=with_schema,
            use_hms=use_hms,
        )

        database_structure_request.additional_properties = d
        return database_structure_request

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
