from dm_bot.config import Settings, get_settings
from dm_bot.models.schemas import HealthSnapshot, ModelTarget


def build_model_snapshot(settings: Settings | None = None) -> HealthSnapshot:
    settings = settings or get_settings()
    router_ready = bool(settings.router_model and settings.ollama_base_url)
    narrator_ready = bool(settings.narrator_model and settings.ollama_base_url)

    return HealthSnapshot(
        status="ok" if router_ready and narrator_ready else "degraded",
        checks={
            "router_model": ModelTarget(
                name=settings.router_model,
                reachable=router_ready,
                detail="configured" if router_ready else "missing configuration",
            ),
            "narrator_model": ModelTarget(
                name=settings.narrator_model,
                reachable=narrator_ready,
                detail="configured" if narrator_ready else "missing configuration",
            ),
        },
    )
