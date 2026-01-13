from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import requests  # type: ignore

from ..config import CapabilityFlags
from ..logging_system import BaseLogger


@dataclass
class WebResult:
    title: str
    url: str
    snippet: str


class WebSearchClient:
    """
    Simple HTTP web search client (Brave-style). Capability-gated.
    """

    def __init__(
        self,
        api_key: Optional[str],
        endpoint: Optional[str],
        capabilities: CapabilityFlags,
        logger: BaseLogger,
    ):
        self.api_key = api_key
        self.endpoint = endpoint or "https://api.search.brave.com/res/v1/web/search"
        self.capabilities = capabilities
        self.logger = logger

    def search(self, query: str, limit: int = 5) -> List[WebResult]:
        if not self.capabilities.can_use_network:
            raise PermissionError("Network/web search not allowed in current mode")
        if not self.api_key:
            raise RuntimeError("Web search API key not configured")

        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "x-subscription-token": self.api_key,
        }
        params = {"q": query, "count": limit}
        self.logger.info("web_search", "Performing web search", query=query, limit=limit)

        resp = requests.get(self.endpoint, headers=headers, params=params, timeout=20)
        resp.raise_for_status()
        data: Dict[str, Any] = resp.json()

        web_results: List[WebResult] = []
        for item in data.get("web", {}).get("results", []):
            web_results.append(
                WebResult(
                    title=item.get("title", ""),
                    url=item.get("url", ""),
                    snippet=item.get("description", "") or "",
                )
            )

        self.logger.info(
            "web_search",
            "Web search completed",
            query=query,
            results=len(web_results),
        )
        return web_results
