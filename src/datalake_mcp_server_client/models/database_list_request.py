from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseListRequest")


@_attrs_define
class DatabaseListRequest:
    """Request model for listing databases.

    Attributes:
        use_hms (bool | Unset): Whether to use Hive Metastore client for faster metadata retrieval Default: True.
        filter_by_namespace (bool | Unset): Whether to filter databases by user/tenant namespace prefixes Default: True.
    """

    use_hms: bool | Unset = True
    filter_by_namespace: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_hms = self.use_hms

        filter_by_namespace = self.filter_by_namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use_hms is not UNSET:
            field_dict["use_hms"] = use_hms
        if filter_by_namespace is not UNSET:
            field_dict["filter_by_namespace"] = filter_by_namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        use_hms = d.pop("use_hms", UNSET)

        filter_by_namespace = d.pop("filter_by_namespace", UNSET)

        database_list_request = cls(
            use_hms=use_hms,
            filter_by_namespace=filter_by_namespace,
        )

        database_list_request.additional_properties = d
        return database_list_request

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
