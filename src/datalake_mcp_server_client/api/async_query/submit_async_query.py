from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_query_submit_request import AsyncQuerySubmitRequest
from ...models.async_query_submit_response import AsyncQuerySubmitResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AsyncQuerySubmitRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/delta/tables/query/async/submit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AsyncQuerySubmitResponse | ErrorResponse | None:
    if response.status_code == 202:
        response_202 = AsyncQuerySubmitResponse.from_dict(response.json())

        return response_202

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
) -> Response[AsyncQuerySubmitResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AsyncQuerySubmitRequest,
) -> Response[AsyncQuerySubmitResponse | ErrorResponse]:
    """Submit an async query

     Submits a Spark SQL query for asynchronous execution. Returns a job_id immediately. Poll
    /{job_id}/status to track progress, then call /{job_id}/results to retrieve the data inline (same
    format as the sync query endpoint). Supports pagination with limit (max 5000) and offset parameters.

    Args:
        body (AsyncQuerySubmitRequest): Request model for submitting an async query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncQuerySubmitResponse | ErrorResponse]
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
    body: AsyncQuerySubmitRequest,
) -> AsyncQuerySubmitResponse | ErrorResponse | None:
    """Submit an async query

     Submits a Spark SQL query for asynchronous execution. Returns a job_id immediately. Poll
    /{job_id}/status to track progress, then call /{job_id}/results to retrieve the data inline (same
    format as the sync query endpoint). Supports pagination with limit (max 5000) and offset parameters.

    Args:
        body (AsyncQuerySubmitRequest): Request model for submitting an async query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncQuerySubmitResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AsyncQuerySubmitRequest,
) -> Response[AsyncQuerySubmitResponse | ErrorResponse]:
    """Submit an async query

     Submits a Spark SQL query for asynchronous execution. Returns a job_id immediately. Poll
    /{job_id}/status to track progress, then call /{job_id}/results to retrieve the data inline (same
    format as the sync query endpoint). Supports pagination with limit (max 5000) and offset parameters.

    Args:
        body (AsyncQuerySubmitRequest): Request model for submitting an async query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncQuerySubmitResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AsyncQuerySubmitRequest,
) -> AsyncQuerySubmitResponse | ErrorResponse | None:
    """Submit an async query

     Submits a Spark SQL query for asynchronous execution. Returns a job_id immediately. Poll
    /{job_id}/status to track progress, then call /{job_id}/results to retrieve the data inline (same
    format as the sync query endpoint). Supports pagination with limit (max 5000) and offset parameters.

    Args:
        body (AsyncQuerySubmitRequest): Request model for submitting an async query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncQuerySubmitResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
