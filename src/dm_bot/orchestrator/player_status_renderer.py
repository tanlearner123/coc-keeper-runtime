"""Player status rendering for Discord surfaces.

This module provides renderers that transform VisibilitySnapshot data
into player-facing Discord messages for the status/info channel and
concise game channel presence.
"""

from dm_bot.orchestrator.visibility import (
    VisibilitySnapshot,
    WaitingReasonCode,
    PlayerSnapshot,
    SessionPhase,
)


class PlayerStatusRenderer:
    """Renders VisibilitySnapshot for player-facing status surfaces."""

    def __init__(self, active_characters: dict[str, str] | None = None) -> None:
        self._active_characters = active_characters or {}

    def render_overview(self, snapshot: VisibilitySnapshot | None) -> str:
        """Render medium-density overview panel for player status channel.

        Displays:
        - Structured header (Campaign/Adventure/Session)
        - Short narrative/status line
        - Participation summary (ready/submitted/pending)
        - Wait reasons with pending users
        """
        if snapshot is None:
            return self._render_inactive_no_session()

        # Check for inactive states
        if not snapshot.campaign.campaign_id:
            return self._render_inactive_no_session()

        return self._render_active_overview(snapshot)

    def render_concise(self, snapshot: VisibilitySnapshot | None) -> str:
        """Render concise status for game channel presence.

        Displays only:
        - Structured header
        - Short narrative line
        - Immediate wait reason
        """
        if snapshot is None:
            return self._render_inactive_no_session()

        if not snapshot.campaign.campaign_id:
            return self._render_inactive_no_session()

        return self._render_concise_status(snapshot)

    def render_personal_detail(
        self, snapshot: VisibilitySnapshot | None, user_id: str
    ) -> str:
        """Render detailed personal state for a specific player.

        Returns ephemeral/private message with:
        - Character name and role
        - HP, SAN, MP, Luck
        - Ready/submitted status
        """
        if snapshot is None:
            return self._render_inactive_no_session()

        if not snapshot.campaign.campaign_id:
            return self._render_inactive_no_session()

        # Find the player's snapshot
        player = self._find_player(snapshot, user_id)
        if player is None:
            return f"你在当前战役中没有角色记录。"

        return self._render_player_detail(player)

    def _render_active_overview(self, snapshot: VisibilitySnapshot) -> str:
        """Render the active session overview."""
        lines = []

        # Header section
        lines.append("📋 **当前战役状态**")
        lines.append("")
        lines.append(f"**战役 ID:** `{snapshot.campaign.campaign_id}`")

        # Adventure/Scene info if available
        if snapshot.adventure.adventure_id:
            lines.append(f"**模组:** `{snapshot.adventure.adventure_id}`")
        if snapshot.adventure.scene_id:
            lines.append(f"**场景:** `{snapshot.adventure.scene_id}`")

        # Session phase
        phase_emoji = self._phase_emoji(snapshot.session.phase)
        lines.append(f"{phase_emoji} **阶段:** {snapshot.session.phase.value}")
        lines.append("")

        # Narrative line
        narrative = self._build_narrative_line(snapshot)
        lines.append(f"_{narrative}_")
        lines.append("")

        # Participation summary
        lines.append("**玩家状态:**")
        lines.append(self._build_participation_summary(snapshot))
        lines.append("")

        # Wait reasons
        wait_block = self._build_wait_block(snapshot)
        if wait_block:
            lines.append("**等待状态:**")
            lines.append(wait_block)

        return "\n".join(lines)

    def _render_concise_status(self, snapshot: VisibilitySnapshot) -> str:
        """Render concise status for game channel."""
        lines = []

        # Brief header
        campaign = snapshot.campaign.campaign_id
        phase = snapshot.session.phase.value

        lines.append(f"🎮 **{campaign}** | {phase}")

        # Short narrative line
        narrative = self._build_narrative_line(snapshot)
        lines.append(f"_{narrative}_")

        # Wait reason (if any)
        if snapshot.waiting.reason_code != WaitingReasonCode.NONE:
            lines.append(f"⏳ {snapshot.waiting.message}")

        return "\n".join(lines)

    def _render_player_detail(self, player: PlayerSnapshot) -> str:
        """Render detailed personal state for a player."""
        lines = []

        character_name = self._active_characters.get(player.user_id, player.name)

        lines.append(f"**{character_name}** ({player.role})")
        if player.occupation:
            lines.append(f"职业: {player.occupation}")
        lines.append("")

        # Stats
        lines.append("**属性:**")
        lines.append(f"❤️ HP: {player.hp}")
        lines.append(f"🧠 SAN: {player.san}")
        lines.append(f"💧 MP: {player.mp}")
        lines.append(f"🍀 幸运: {player.luck}")
        lines.append("")

        # Status
        status_parts = []
        if player.is_ready:
            status_parts.append("✅ 已就位")
        if player.has_submitted_action:
            status_parts.append("📝 已提交行动")
        if not player.onboarding_complete:
            status_parts.append("📋 待规则确认")

        if status_parts:
            lines.append("**状态:** " + " | ".join(status_parts))
        else:
            lines.append("**状态:** 正常")

        return "\n".join(lines)

    def _render_inactive_no_session(self) -> str:
        """Render inactive/unloaded state message."""
        return (
            "🔕 **当前没有活跃战役**\n\n"
            "目前没有正在进行的游戏会话。\n\n"
            "**如何开始:**\n"
            "1. 在游戏大厅使用 `/bind_campaign` 绑定战役\n"
            "2. 玩家使用 `/join_campaign` 加入\n"
            "3. 管理员使用 `/load_adventure` 加载模组\n"
            "4. 玩家使用 `/ready` 就位\n"
            "5. 管理员使用 `/start-session` 开始游戏"
        )

    def _render_inactive_not_loaded(self) -> str:
        """Render state when session exists but adventure not loaded."""
        return (
            "⏸️ **战役已建立，模组未加载**\n\n"
            "当前战役已创建，但还没有加载模组。\n"
            "管理员可以使用 `/load_adventure` 加载模组。"
        )

    def _find_player(
        self, snapshot: VisibilitySnapshot, user_id: str
    ) -> PlayerSnapshot | None:
        """Find a player's snapshot by user_id."""
        for player in snapshot.players.players:
            if player.user_id == user_id:
                return player
        return None

    def _phase_emoji(self, phase: SessionPhase) -> str:
        """Get emoji for session phase."""
        phase_emojis = {
            SessionPhase.LOBBY: "🏠",
            SessionPhase.ONBOARDING: "📋",
            SessionPhase.AWAITING_READY: "✋",
            SessionPhase.AWAITING_ADMIN_START: "👑",
            SessionPhase.SCENE_ROUND_OPEN: "🎭",
            SessionPhase.SCENE_ROUND_RESOLVING: "⚙️",
            SessionPhase.COMBAT: "⚔️",
            SessionPhase.PAUSED: "⏸️",
        }
        return phase_emojis.get(phase, "❓")

    def _build_narrative_line(self, snapshot: VisibilitySnapshot) -> str:
        """Build a short narrative/status line describing current state."""
        ready = snapshot.session.ready_count
        total = snapshot.session.total_members

        if snapshot.session.phase == SessionPhase.LOBBY:
            return f"等待玩家加入和就位 ({ready}/{total})"

        if snapshot.session.phase == SessionPhase.ONBOARDING:
            return "正在进行规则介绍"

        if snapshot.session.phase == SessionPhase.AWAITING_READY:
            return f"等待玩家就位 ({ready}/{total})"

        if snapshot.session.phase == SessionPhase.AWAITING_ADMIN_START:
            return "等待管理员开始游戏"

        if snapshot.session.phase == SessionPhase.SCENE_ROUND_OPEN:
            return f"行动收集阶段 - {ready}/{total} 已提交"

        if snapshot.session.phase == SessionPhase.SCENE_ROUND_RESOLVING:
            return "KP 正在结算回合"

        if snapshot.session.phase == SessionPhase.COMBAT:
            return "战斗中"

        if snapshot.session.phase == SessionPhase.PAUSED:
            return "游戏已暂停"

        return f"阶段: {snapshot.session.phase.value}"

    def _build_participation_summary(self, snapshot: VisibilitySnapshot) -> str:
        """Build participation summary showing ready/submitted/pending."""
        players = snapshot.players.players
        if not players:
            return "无玩家"

        ready = []
        pending = []
        submitted = []

        for player in players:
            name = self._active_characters.get(player.user_id, player.name)
            if player.is_ready:
                ready.append(name)
            if player.has_submitted_action:
                submitted.append(name)
            if not player.is_ready and player.onboarding_complete:
                pending.append(name)

        parts = []
        if ready:
            parts.append(f"✅ 已就位: {', '.join(ready)}")
        if submitted:
            parts.append(f"📝 已行动: {', '.join(submitted)}")
        if pending:
            parts.append(f"⏳ 待行动: {', '.join(pending)}")

        return "\n".join(parts) if parts else "无玩家"

    def _build_wait_block(self, snapshot: VisibilitySnapshot) -> str | None:
        """Build wait reason block showing who/what is pending."""
        reason = snapshot.waiting.reason_code
        if reason == WaitingReasonCode.NONE:
            return None

        message = snapshot.waiting.message

        # Add pending user names if available
        pending_ids = snapshot.waiting.metadata.get("pending_user_ids", [])
        if pending_ids:
            pending_names = []
            for uid in pending_ids:
                name = self._active_characters.get(uid, uid)
                pending_names.append(name)
            if pending_names:
                message += f"\n等待: {', '.join(pending_names)}"

        return message
