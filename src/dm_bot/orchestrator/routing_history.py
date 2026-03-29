from collections import deque
from datetime import datetime

from dm_bot.orchestrator.visibility import RoutingHistoryEntry, RoutingOutcome


class RoutingHistoryStore:
    def __init__(self, max_entries: int = 10) -> None:
        self._max_entries = max_entries
        self._entries: deque[RoutingHistoryEntry] = deque(maxlen=max_entries)

    def add_entry(
        self,
        user_id: str,
        intent: str,
        outcome: RoutingOutcome,
        explanation: str | None = None,
    ) -> None:
        entry = RoutingHistoryEntry(
            timestamp=datetime.now(),
            user_id=user_id,
            intent=intent,
            outcome=outcome,
            explanation=explanation,
        )
        self._entries.append(entry)

    def get_recent(self, n: int = 10) -> list[RoutingHistoryEntry]:
        result = list(self._entries)
        return result[-n:] if n < len(result) else result

    def clear(self) -> None:
        self._entries.clear()

    def __len__(self) -> int:
        return len(self._entries)
