"""A client library for accessing BERDL Datalake MCP Server"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
