from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_by_spec_direction import OrderBySpecDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderBySpec")


@_attrs_define
class OrderBySpec:
    """Model for ORDER BY clause specification.

    Attributes:
        column (str): Column name to sort by
        direction (OrderBySpecDirection | Unset): Sort direction Default: OrderBySpecDirection.ASC.
    """

    column: str
    direction: OrderBySpecDirection | Unset = OrderBySpecDirection.ASC
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column = self.column

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column": column,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column = d.pop("column")

        _direction = d.pop("direction", UNSET)
        direction: OrderBySpecDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = OrderBySpecDirection(_direction)

        order_by_spec = cls(
            column=column,
            direction=direction,
        )

        order_by_spec.additional_properties = d
        return order_by_spec

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
