import json

from pydantic import ValidationError

from dm_bot.models.schemas import ModelRequest, TurnEnvelope
from dm_bot.router.contracts import TurnPlan


class RouterError(RuntimeError):
    pass


class RouterService:
    def __init__(self, client) -> None:
        self._client = client

    async def route(self, envelope: TurnEnvelope) -> TurnPlan:
        request = ModelRequest(
            system_prompt=(
                "You are the routing model for a Discord D&D DM runtime. "
                "Return only valid JSON matching the TurnPlan schema."
            ),
            user_prompt=(
                f"trace_id={envelope.trace_id}\n"
                f"campaign_id={envelope.campaign_id}\n"
                f"channel_id={envelope.channel_id}\n"
                f"user_id={envelope.user_id}\n"
                f"player_input={envelope.content}"
            ),
        )
        response = await self._client.call_router(request)
        try:
            payload = json.loads(response.content)
            return TurnPlan.model_validate(payload)
        except (json.JSONDecodeError, ValidationError) as exc:
            raise RouterError("router returned invalid structured output") from exc
