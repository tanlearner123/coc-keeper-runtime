import asyncio
from uuid import uuid4

from pydantic import BaseModel, Field

from dm_bot.models.schemas import TurnEnvelope


class TurnDispatchResult(BaseModel):
    trace_id: str = Field(min_length=1)
    reply: str = Field(min_length=1)


class TurnRequest(BaseModel):
    campaign_id: str
    channel_id: str
    user_id: str
    content: str = Field(min_length=1)
    trace_id: str | None = None


class TurnCoordinator:
    def __init__(self, *, turn_runner) -> None:
        self._turn_runner = turn_runner
        self._locks: dict[str, asyncio.Lock] = {}

    async def handle_turn(
        self,
        request: TurnRequest | None = None,
        *,
        campaign_id: str | None = None,
        channel_id: str | None = None,
        user_id: str | None = None,
        content: str | None = None,
    ) -> TurnDispatchResult:
        request = request or TurnRequest(
            campaign_id=campaign_id or "",
            channel_id=channel_id or "",
            user_id=user_id or "",
            content=content or "",
        )
        trace_id = request.trace_id or str(uuid4())
        lock = self._locks.setdefault(request.campaign_id, asyncio.Lock())
        async with lock:
            result = await self._turn_runner.run_turn(
                TurnEnvelope(
                    campaign_id=request.campaign_id,
                    channel_id=request.channel_id,
                    user_id=request.user_id,
                    trace_id=trace_id,
                    content=request.content,
                )
            )
        return TurnDispatchResult(trace_id=trace_id, reply=result.reply)
