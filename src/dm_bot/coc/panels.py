from pydantic import BaseModel, Field


class InvestigatorPanel(BaseModel):
    user_id: str
    name: str
    role: str = "investigator"
    occupation: str = ""
    san: int = 50
    hp: int = 10
    mp: int = 10
    luck: int = 50
    skills: dict[str, int] = Field(default_factory=dict)
    journal: list[str] = Field(default_factory=list)
    module_flags: dict[str, str | int | bool] = Field(default_factory=dict)

    def summary(self, *, knowledge_titles: list[str]) -> str:
        lines = [
            f"调查员：{self.name}",
            f"角色类型：{self.role}",
            f"职业：{self.occupation or '未设定'}",
            f"SAN={self.san} HP={self.hp} MP={self.mp} LUCK={self.luck}",
        ]
        if self.skills:
            top_skills = ", ".join(f"{key}:{value}" for key, value in list(self.skills.items())[:6])
            lines.append(f"技能：{top_skills}")
        if knowledge_titles:
            lines.append(f"已知线索：{', '.join(knowledge_titles)}")
        if self.journal:
            lines.append(f"最近记录：{self.journal[-1]}")
        return "\n".join(lines)
