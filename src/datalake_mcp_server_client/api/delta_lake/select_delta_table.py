from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.table_select_request import TableSelectRequest
from ...models.table_select_response import TableSelectResponse
from ...types import Response


def _get_kwargs(
    *,
    body: TableSelectRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/delta/tables/select",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | TableSelectResponse | None:
    if response.status_code == 200:
        response_200 = TableSelectResponse.from_dict(response.json())

        return response_200

    if 400 <= response.status_code <= 499:
        response_4xx = ErrorResponse.from_dict(response.json())

        return response_4xx

    if 500 <= response.status_code <= 599:
        response_5xx = ErrorResponse.from_dict(response.json())

        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | TableSelectResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TableSelectRequest,
) -> Response[ErrorResponse | TableSelectResponse]:
    """Execute a structured SELECT query

     Builds and executes a SELECT query from structured parameters. Supports column selection,
    aggregations (COUNT, SUM, AVG, MIN, MAX), JOINs, WHERE filters, GROUP BY, HAVING, ORDER BY,
    DISTINCT, and pagination. The backend builds the query safely, preventing SQL injection.

    Args:
        body (TableSelectRequest): Request model for structured SELECT query builder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TableSelectResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: TableSelectRequest,
) -> ErrorResponse | TableSelectResponse | None:
    """Execute a structured SELECT query

     Builds and executes a SELECT query from structured parameters. Supports column selection,
    aggregations (COUNT, SUM, AVG, MIN, MAX), JOINs, WHERE filters, GROUP BY, HAVING, ORDER BY,
    DISTINCT, and pagination. The backend builds the query safely, preventing SQL injection.

    Args:
        body (TableSelectRequest): Request model for structured SELECT query builder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TableSelectResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TableSelectRequest,
) -> Response[ErrorResponse | TableSelectResponse]:
    """Execute a structured SELECT query

     Builds and executes a SELECT query from structured parameters. Supports column selection,
    aggregations (COUNT, SUM, AVG, MIN, MAX), JOINs, WHERE filters, GROUP BY, HAVING, ORDER BY,
    DISTINCT, and pagination. The backend builds the query safely, preventing SQL injection.

    Args:
        body (TableSelectRequest): Request model for structured SELECT query builder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TableSelectResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TableSelectRequest,
) -> ErrorResponse | TableSelectResponse | None:
    """Execute a structured SELECT query

     Builds and executes a SELECT query from structured parameters. Supports column selection,
    aggregations (COUNT, SUM, AVG, MIN, MAX), JOINs, WHERE filters, GROUP BY, HAVING, ORDER BY,
    DISTINCT, and pagination. The backend builds the query safely, preventing SQL injection.

    Args:
        body (TableSelectRequest): Request model for structured SELECT query builder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TableSelectResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
