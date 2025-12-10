from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deep_health_response import DeepHealthResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/health",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeepHealthResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeepHealthResponse.from_dict(response.json())

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
) -> Response[DeepHealthResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeepHealthResponse | ErrorResponse]:
    """Health check

     Returns detailed health status of all backend services including Redis, PostgreSQL (if configured),
    and Hive Metastore Thrift connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepHealthResponse | ErrorResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> DeepHealthResponse | ErrorResponse | None:
    """Health check

     Returns detailed health status of all backend services including Redis, PostgreSQL (if configured),
    and Hive Metastore Thrift connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepHealthResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeepHealthResponse | ErrorResponse]:
    """Health check

     Returns detailed health status of all backend services including Redis, PostgreSQL (if configured),
    and Hive Metastore Thrift connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepHealthResponse | ErrorResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> DeepHealthResponse | ErrorResponse | None:
    """Health check

     Returns detailed health status of all backend services including Redis, PostgreSQL (if configured),
    and Hive Metastore Thrift connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepHealthResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
