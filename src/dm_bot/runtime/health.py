from dm_bot.config import Settings
from dm_bot.models.schemas import HealthSnapshot
from dm_bot.runtime.model_checks import build_model_snapshot


def build_health_snapshot(settings: Settings | None = None) -> HealthSnapshot:
    return build_model_snapshot(settings)
