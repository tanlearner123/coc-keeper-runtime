class DiagnosticsService:
    def __init__(self, store) -> None:
        self._store = store

    def recent_summary(self, campaign_id: str) -> str:
        events = self._store.list_events(campaign_id)
        if not events:
            return "no events"
        last = events[-5:]
        return "\n".join(f"{event['trace_id']} {event['event_type']}" for event in last)
