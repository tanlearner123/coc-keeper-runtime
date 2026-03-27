from typing import Protocol

import d20
from pydantic import BaseModel, Field

from dm_bot.rules.actions import AdvantageMode


class DiceOutcome(BaseModel):
    expression: str = Field(min_length=1)
    total: int
    rendered: str = Field(min_length=1)


class DiceRoller(Protocol):
    def roll(self, expression: str, *, advantage: AdvantageMode = "none") -> DiceOutcome: ...


class D20DiceRoller:
    _ADVANTAGE_MAP = {
        "none": d20.AdvType.NONE,
        "advantage": d20.AdvType.ADV,
        "disadvantage": d20.AdvType.DIS,
    }

    def roll(self, expression: str, *, advantage: AdvantageMode = "none") -> DiceOutcome:
        try:
            result = d20.roll(expression, advantage=self._ADVANTAGE_MAP[advantage])
        except Exception as exc:  # pragma: no cover - d20 exception types vary
            raise ValueError(str(exc)) from exc
        return DiceOutcome(expression=expression, total=int(result.total), rendered=str(result))
