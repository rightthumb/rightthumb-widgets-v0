from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, List

from .memory import MemoryStore, MemoryEvent


@dataclass
class StrategySuggestion:
    description: str
    rationale: str
    related_events: List[MemoryEvent]


class MetaCognitionEngine:
    """
    Metacognition engine that records events and provides simple heuristic
    suggestions based on past experience.

    Embedding/vector DB integration can be layered on top later by extending
    this class or plugging in a different engine that respects the same API.
    """

    def __init__(self, memory_store: MemoryStore):
        self._memory = memory_store

    def record_event(
        self,
        kind: str,
        session_id: Optional[str],
        project_goal: Optional[str],
        language: Optional[str],
        summary: str,
        **metadata: Any,
    ) -> None:
        ev = MemoryEvent(
            timestamp=time.time(),
            kind=kind,
            session_id=session_id,
            project_goal=project_goal,
            language=language,
            summary=summary,
            metadata=metadata,
        )
        self._memory.record(ev)

    def record_error(
        self,
        session_id: Optional[str],
        project_goal: Optional[str],
        language: Optional[str],
        error_message: str,
        **metadata: Any,
    ) -> None:
        self.record_event(
            kind="error",
            session_id=session_id,
            project_goal=project_goal,
            language=language,
            summary=error_message,
            **metadata,
        )

    def record_solution(
        self,
        session_id: Optional[str],
        project_goal: Optional[str],
        language: Optional[str],
        summary: str,
        **metadata: Any,
    ) -> None:
        self.record_event(
            kind="solution",
            session_id=session_id,
            project_goal=project_goal,
            language=language,
            summary=summary,
            **metadata,
        )

    def suggest_strategies_for(
        self,
        goal: str,
        language: Optional[str] = None,
        error_signature: Optional[str] = None,
    ) -> StrategySuggestion:
        """
        Very simple heuristic suggestion mechanism that looks at past
        solutions and errors. This is intentionally lightweight; a more
        advanced implementation can use embeddings.
        """
        recent_solutions = self._memory.query(kind="solution", limit=20)
        recent_errors = self._memory.query(kind="error", limit=20)

        related: List[MemoryEvent] = []
        rationale_parts: List[str] = []

        if language:
            related += [ev for ev in recent_solutions if ev.language == language]
        else:
            related += recent_solutions

        if error_signature:
            related += [ev for ev in recent_errors if error_signature in (ev.summary or "")]

        if not related:
            rationale = "No directly related past experience found; defaulting to generic cautious strategy."
            return StrategySuggestion(
                description="Proceed with small steps, test frequently, and log all errors.",
                rationale=rationale,
                related_events=[],
            )

        rationale_parts.append("Found prior solutions and/or errors that may be relevant.")
        description = "Use approaches that previously led to 'solution' events for similar language or errors."

        return StrategySuggestion(
            description=description,
            rationale=" ".join(rationale_parts),
            related_events=related[:10],
        )
