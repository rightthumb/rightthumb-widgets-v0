from __future__ import annotations

import json
import time
import uuid
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class Task:
    description: str
    status: str = "pending"  # pending | in_progress | done | blocked
    notes: List[str] = field(default_factory=list)


@dataclass
class Sprint:
    title: str
    status: str = "active"  # active | done
    tasks: List[Task] = field(default_factory=list)


@dataclass
class Session:
    id: str
    parent_id: Optional[str]
    goal: str
    mode_name: str
    created_at: float
    updated_at: float
    sprints: List[Sprint] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Session":
        sprints: List[Sprint] = []
        for s in data.get("sprints", []):
            tasks = [Task(**t) for t in s.get("tasks", [])]
            sprints.append(Sprint(title=s["title"], status=s.get("status", "active"), tasks=tasks))
        return cls(
            id=data["id"],
            parent_id=data.get("parent_id"),
            goal=data["goal"],
            mode_name=data["mode_name"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            sprints=sprints,
            metadata=data.get("metadata", {}),
        )


class SessionManager:
    """
    File-based session manager with forking support.
    """

    def __init__(self, state_dir: Path):
        self.state_dir = state_dir
        self.sessions_dir = self.state_dir / "sessions"
        self.sessions_dir.mkdir(parents=True, exist_ok=True)

    def _session_file(self, session_id: str) -> Path:
        return self.sessions_dir / f"{session_id}.json"

    def create_session(self, goal: str, mode_name: str, parent_id: Optional[str] = None) -> Session:
        sid = str(uuid.uuid4())
        now = time.time()
        session = Session(
            id=sid,
            parent_id=parent_id,
            goal=goal,
            mode_name=mode_name,
            created_at=now,
            updated_at=now,
            sprints=[],
            metadata={},
        )
        self.save_session(session)
        return session

    def fork_session(self, base_session_id: str) -> Session:
        parent = self.load_session(base_session_id)
        if parent is None:
            raise ValueError(f"Session {base_session_id} not found")
        child = self.create_session(
            goal=parent.goal,
            mode_name=parent.mode_name,
            parent_id=parent.id,
        )
        child.metadata["forked_from"] = parent.id
        self.save_session(child)
        return child

    def save_session(self, session: Session) -> None:
        session.updated_at = time.time()
        path = self._session_file(session.id)
        with path.open("w", encoding="utf-8") as f:
            json.dump(session.to_dict(), f, indent=2)

    def load_session(self, session_id: str) -> Optional[Session]:
        path = self._session_file(session_id)
        if not path.exists():
            return None
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return Session.from_dict(data)

    def list_sessions(self) -> List[Session]:
        sessions: List[Session] = []
        for file in self.sessions_dir.glob("*.json"):
            try:
                with file.open("r", encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(Session.from_dict(data))
            except Exception:
                continue
        sessions.sort(key=lambda s: s.created_at)
        return sessions

    def get_session_info(self, session_id: str) -> Optional[Dict[str, Any]]:
        s = self.load_session(session_id)
        if not s:
            return None
        return {
            "id": s.id,
            "parent_id": s.parent_id,
            "goal": s.goal,
            "mode_name": s.mode_name,
            "created_at": s.created_at,
            "updated_at": s.updated_at,
            "num_sprints": len(s.sprints),
        }

    def add_sprint(self, session: Session, sprint: Sprint) -> None:
        session.sprints.append(sprint)
        self.save_session(session)

    def get_active_sprint(self, session: Session) -> Optional[Sprint]:
        for s in session.sprints:
            if s.status == "active":
                return s
        return None

    def complete_sprint_if_done(self, session: Session) -> None:
        sprint = self.get_active_sprint(session)
        if not sprint:
            return
        if all(t.status == "done" for t in sprint.tasks):
            sprint.status = "done"
            self.save_session(session)

    def trim_history(self, session: Session, max_sprints: int = 5) -> None:
        if len(session.sprints) <= max_sprints:
            return
        session.sprints = session.sprints[-max_sprints:]
        self.save_session(session)
