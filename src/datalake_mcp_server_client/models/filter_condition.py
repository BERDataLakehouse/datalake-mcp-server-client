from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_condition_operator import FilterConditionOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterCondition")


@_attrs_define
class FilterCondition:
    """Model for WHERE/HAVING filter conditions.

    Attributes:
        column (str): Column name to filter on
        operator (FilterConditionOperator): Comparison operator
        value (Any | None | Unset): Value for comparison (None for IS NULL/IS NOT NULL)
        values (list[Any] | None | Unset): List of values for IN, NOT IN, or BETWEEN operators
    """

    column: str
    operator: FilterConditionOperator
    value: Any | None | Unset = UNSET
    values: list[Any] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column = self.column

        operator = self.operator.value

        value: Any | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        values: list[Any] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = self.values

        else:
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column": column,
                "operator": operator,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column = d.pop("column")

        operator = FilterConditionOperator(d.pop("operator"))

        def _parse_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_values(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[Any], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))

        filter_condition = cls(
            column=column,
            operator=operator,
            value=value,
            values=values,
        )

        filter_condition.additional_properties = d
        return filter_condition

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
