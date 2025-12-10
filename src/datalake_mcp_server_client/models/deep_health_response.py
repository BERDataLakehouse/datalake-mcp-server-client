from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deep_health_response_status import DeepHealthResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_health import ComponentHealth


T = TypeVar("T", bound="DeepHealthResponse")


@_attrs_define
class DeepHealthResponse:
    """Health check response with component-level details.

    Attributes:
        status (DeepHealthResponseStatus): Overall health status
        components (list[ComponentHealth]): Health status of each component
        message (None | str | Unset): Summary message about system health
    """

    status: DeepHealthResponseStatus
    components: list[ComponentHealth]
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "components": components,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.component_health import ComponentHealth

        d = dict(src_dict)
        status = DeepHealthResponseStatus(d.pop("status"))

        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = ComponentHealth.from_dict(components_item_data)

            components.append(components_item)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        deep_health_response = cls(
            status=status,
            components=components,
            message=message,
        )

        deep_health_response.additional_properties = d
        return deep_health_response

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
