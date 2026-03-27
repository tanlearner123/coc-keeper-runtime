from pydantic import BaseModel, Field

from dm_bot.models.schemas import TurnEnvelope
from dm_bot.narration.service import NarrationRequest
from dm_bot.router.contracts import TurnPlan


class TurnResult(BaseModel):
    plan: TurnPlan
    reply: str = Field(min_length=1)


class TurnRunner:
    def __init__(self, *, router, narrator) -> None:
        self._router = router
        self._narrator = narrator

    async def run_turn(
        self,
        envelope: TurnEnvelope,
        *,
        tool_results: list[dict[str, object]] | None = None,
        state_snapshot: dict[str, object] | None = None,
    ) -> TurnResult:
        plan = await self._router.route(envelope)
        reply = await self._narrator.narrate(
            NarrationRequest(
                player_input=envelope.content,
                state_snapshot=state_snapshot or {},
                tool_results=tool_results or [],
                plan=plan,
            )
        )
        return TurnResult(plan=plan, reply=reply)
