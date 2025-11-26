from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aggregation_spec_function import AggregationSpecFunction
from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregationSpec")


@_attrs_define
class AggregationSpec:
    """Model for aggregation function specification.

    Attributes:
        function (AggregationSpecFunction): Aggregation function to apply
        column (str): Column to aggregate, or '*' for COUNT(*)
        alias (None | str | Unset): Output alias for the aggregation result
    """

    function: AggregationSpecFunction
    column: str
    alias: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function = self.function.value

        column = self.column

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function": function,
                "column": column,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        function = AggregationSpecFunction(d.pop("function"))

        column = d.pop("column")

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        aggregation_spec = cls(
            function=function,
            column=column,
            alias=alias,
        )

        aggregation_spec.additional_properties = d
        return aggregation_spec

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
