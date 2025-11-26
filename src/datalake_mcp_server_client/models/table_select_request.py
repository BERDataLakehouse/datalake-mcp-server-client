from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_spec import AggregationSpec
    from ..models.column_spec import ColumnSpec
    from ..models.filter_condition import FilterCondition
    from ..models.join_clause import JoinClause
    from ..models.order_by_spec import OrderBySpec


T = TypeVar("T", bound="TableSelectRequest")


@_attrs_define
class TableSelectRequest:
    """Request model for structured SELECT query builder.

    Attributes:
        database (str): Name of the primary database containing the table
        table (str): Name of the primary table to query
        joins (list[JoinClause] | None | Unset): Optional list of JOIN clauses
        columns (list[ColumnSpec] | None | Unset): Columns to select (None for SELECT *)
        distinct (bool | Unset): Whether to apply DISTINCT to results Default: False.
        aggregations (list[AggregationSpec] | None | Unset): Optional aggregation functions to apply
        filters (list[FilterCondition] | None | Unset): Optional WHERE clause conditions
        group_by (list[str] | None | Unset): Optional columns to GROUP BY
        having (list[FilterCondition] | None | Unset): Optional HAVING clause conditions (filters after GROUP BY)
        order_by (list[OrderBySpec] | None | Unset): Optional ORDER BY specifications
        limit (int | Unset): Maximum number of rows to return Default: 100.
        offset (int | Unset): Number of rows to skip for pagination Default: 0.
    """

    database: str
    table: str
    joins: list[JoinClause] | None | Unset = UNSET
    columns: list[ColumnSpec] | None | Unset = UNSET
    distinct: bool | Unset = False
    aggregations: list[AggregationSpec] | None | Unset = UNSET
    filters: list[FilterCondition] | None | Unset = UNSET
    group_by: list[str] | None | Unset = UNSET
    having: list[FilterCondition] | None | Unset = UNSET
    order_by: list[OrderBySpec] | None | Unset = UNSET
    limit: int | Unset = 100
    offset: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database = self.database

        table = self.table

        joins: list[dict[str, Any]] | None | Unset
        if isinstance(self.joins, Unset):
            joins = UNSET
        elif isinstance(self.joins, list):
            joins = []
            for joins_type_0_item_data in self.joins:
                joins_type_0_item = joins_type_0_item_data.to_dict()
                joins.append(joins_type_0_item)

        else:
            joins = self.joins

        columns: list[dict[str, Any]] | None | Unset
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, list):
            columns = []
            for columns_type_0_item_data in self.columns:
                columns_type_0_item = columns_type_0_item_data.to_dict()
                columns.append(columns_type_0_item)

        else:
            columns = self.columns

        distinct = self.distinct

        aggregations: list[dict[str, Any]] | None | Unset
        if isinstance(self.aggregations, Unset):
            aggregations = UNSET
        elif isinstance(self.aggregations, list):
            aggregations = []
            for aggregations_type_0_item_data in self.aggregations:
                aggregations_type_0_item = aggregations_type_0_item_data.to_dict()
                aggregations.append(aggregations_type_0_item)

        else:
            aggregations = self.aggregations

        filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)

        else:
            filters = self.filters

        group_by: list[str] | None | Unset
        if isinstance(self.group_by, Unset):
            group_by = UNSET
        elif isinstance(self.group_by, list):
            group_by = self.group_by

        else:
            group_by = self.group_by

        having: list[dict[str, Any]] | None | Unset
        if isinstance(self.having, Unset):
            having = UNSET
        elif isinstance(self.having, list):
            having = []
            for having_type_0_item_data in self.having:
                having_type_0_item = having_type_0_item_data.to_dict()
                having.append(having_type_0_item)

        else:
            having = self.having

        order_by: list[dict[str, Any]] | None | Unset
        if isinstance(self.order_by, Unset):
            order_by = UNSET
        elif isinstance(self.order_by, list):
            order_by = []
            for order_by_type_0_item_data in self.order_by:
                order_by_type_0_item = order_by_type_0_item_data.to_dict()
                order_by.append(order_by_type_0_item)

        else:
            order_by = self.order_by

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database": database,
                "table": table,
            }
        )
        if joins is not UNSET:
            field_dict["joins"] = joins
        if columns is not UNSET:
            field_dict["columns"] = columns
        if distinct is not UNSET:
            field_dict["distinct"] = distinct
        if aggregations is not UNSET:
            field_dict["aggregations"] = aggregations
        if filters is not UNSET:
            field_dict["filters"] = filters
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if having is not UNSET:
            field_dict["having"] = having
        if order_by is not UNSET:
            field_dict["order_by"] = order_by
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregation_spec import AggregationSpec
        from ..models.column_spec import ColumnSpec
        from ..models.filter_condition import FilterCondition
        from ..models.join_clause import JoinClause
        from ..models.order_by_spec import OrderBySpec

        d = dict(src_dict)
        database = d.pop("database")

        table = d.pop("table")

        def _parse_joins(data: object) -> list[JoinClause] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                joins_type_0 = []
                _joins_type_0 = data
                for joins_type_0_item_data in _joins_type_0:
                    joins_type_0_item = JoinClause.from_dict(joins_type_0_item_data)

                    joins_type_0.append(joins_type_0_item)

                return joins_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JoinClause] | None | Unset, data)

        joins = _parse_joins(d.pop("joins", UNSET))

        def _parse_columns(data: object) -> list[ColumnSpec] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = []
                _columns_type_0 = data
                for columns_type_0_item_data in _columns_type_0:
                    columns_type_0_item = ColumnSpec.from_dict(columns_type_0_item_data)

                    columns_type_0.append(columns_type_0_item)

                return columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ColumnSpec] | None | Unset, data)

        columns = _parse_columns(d.pop("columns", UNSET))

        distinct = d.pop("distinct", UNSET)

        def _parse_aggregations(data: object) -> list[AggregationSpec] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aggregations_type_0 = []
                _aggregations_type_0 = data
                for aggregations_type_0_item_data in _aggregations_type_0:
                    aggregations_type_0_item = AggregationSpec.from_dict(
                        aggregations_type_0_item_data
                    )

                    aggregations_type_0.append(aggregations_type_0_item)

                return aggregations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AggregationSpec] | None | Unset, data)

        aggregations = _parse_aggregations(d.pop("aggregations", UNSET))

        def _parse_filters(data: object) -> list[FilterCondition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in _filters_type_0:
                    filters_type_0_item = FilterCondition.from_dict(
                        filters_type_0_item_data
                    )

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterCondition] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_group_by(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_by_type_0 = cast(list[str], data)

                return group_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_by = _parse_group_by(d.pop("group_by", UNSET))

        def _parse_having(data: object) -> list[FilterCondition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                having_type_0 = []
                _having_type_0 = data
                for having_type_0_item_data in _having_type_0:
                    having_type_0_item = FilterCondition.from_dict(
                        having_type_0_item_data
                    )

                    having_type_0.append(having_type_0_item)

                return having_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterCondition] | None | Unset, data)

        having = _parse_having(d.pop("having", UNSET))

        def _parse_order_by(data: object) -> list[OrderBySpec] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                order_by_type_0 = []
                _order_by_type_0 = data
                for order_by_type_0_item_data in _order_by_type_0:
                    order_by_type_0_item = OrderBySpec.from_dict(
                        order_by_type_0_item_data
                    )

                    order_by_type_0.append(order_by_type_0_item)

                return order_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrderBySpec] | None | Unset, data)

        order_by = _parse_order_by(d.pop("order_by", UNSET))

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        table_select_request = cls(
            database=database,
            table=table,
            joins=joins,
            columns=columns,
            distinct=distinct,
            aggregations=aggregations,
            filters=filters,
            group_by=group_by,
            having=having,
            order_by=order_by,
            limit=limit,
            offset=offset,
        )

        table_select_request.additional_properties = d
        return table_select_request

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
