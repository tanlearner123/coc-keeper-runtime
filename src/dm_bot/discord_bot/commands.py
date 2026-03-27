import json

from dm_bot.config import Settings
from dm_bot.runtime.health import build_health_snapshot


class BotCommands:
    def __init__(self, *, settings: Settings, session_store, turn_coordinator) -> None:
        self._settings = settings
        self._session_store = session_store
        self._turn_coordinator = turn_coordinator

    async def setup_check(self, interaction) -> None:
        snapshot = build_health_snapshot(self._settings)
        await interaction.response.send_message(
            json.dumps(snapshot.model_dump(), ensure_ascii=False),
            ephemeral=True,
        )

    async def bind_campaign(self, interaction, *, campaign_id: str) -> None:
        self._session_store.bind_campaign(
            campaign_id=campaign_id,
            channel_id=str(interaction.channel_id),
            guild_id=str(interaction.guild_id),
            owner_id=str(interaction.user.id),
        )
        await interaction.response.send_message(
            f"campaign `{campaign_id}` bound to channel `{interaction.channel_id}`",
            ephemeral=True,
        )

    async def join_campaign(self, interaction) -> None:
        session = self._session_store.join_campaign(
            channel_id=str(interaction.channel_id),
            user_id=str(interaction.user.id),
        )
        await interaction.response.send_message(
            f"joined campaign `{session.campaign_id}`",
            ephemeral=True,
        )

    async def take_turn(self, interaction, *, content: str) -> None:
        session = self._session_store.get_by_channel(str(interaction.channel_id))
        if session is None:
            await interaction.response.send_message(
                "no campaign bound to this channel",
                ephemeral=True,
            )
            return

        await interaction.response.defer(thinking=True)
        result = await self._turn_coordinator.handle_turn(
            campaign_id=session.campaign_id,
            channel_id=str(interaction.channel_id),
            user_id=str(interaction.user.id),
            content=content,
        )
        await interaction.followup.send(result.reply)
