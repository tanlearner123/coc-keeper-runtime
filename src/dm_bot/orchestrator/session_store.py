from pydantic import BaseModel, Field


class CampaignSession(BaseModel):
    campaign_id: str
    channel_id: str
    guild_id: str
    owner_id: str
    member_ids: set[str] = Field(default_factory=set)


class SessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, CampaignSession] = {}

    def bind_campaign(self, *, campaign_id: str, channel_id: str, guild_id: str, owner_id: str) -> CampaignSession:
        session = CampaignSession(
            campaign_id=campaign_id,
            channel_id=channel_id,
            guild_id=guild_id,
            owner_id=owner_id,
            member_ids={owner_id},
        )
        self._sessions[channel_id] = session
        return session

    def join_campaign(self, *, channel_id: str, user_id: str) -> CampaignSession:
        session = self._sessions[channel_id]
        session.member_ids.add(user_id)
        return session

    def get_by_channel(self, channel_id: str) -> CampaignSession | None:
        return self._sessions.get(channel_id)
