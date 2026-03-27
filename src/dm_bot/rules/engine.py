from collections.abc import Callable

from dm_bot.rules.actions import LookupAction, RuleAction
from dm_bot.rules.dice import D20DiceRoller, DiceOutcome


class RulesEngineError(RuntimeError):
    pass


class RulesEngine:
    def __init__(
        self,
        *,
        compendium,
        roll_resolver: Callable[[str], int] | None = None,
        dice_roller=None,
    ) -> None:
        self._compendium = compendium
        if dice_roller is not None:
            self._dice_roller = dice_roller
        elif roll_resolver is not None:
            self._dice_roller = _LegacyDiceRoller(roll_resolver)
        else:
            self._dice_roller = D20DiceRoller()

    def lookup(self, action: LookupAction) -> dict[str, object]:
        try:
            return self._compendium.lookup(action)
        except (ValueError, KeyError) as exc:
            raise RulesEngineError(str(exc)) from exc

    def execute(self, action: RuleAction) -> dict[str, object]:
        if action.action == "attack_roll":
            return self._execute_attack_roll(action)
        if action.action == "ability_check":
            return self._execute_check_like(action, kind="ability_check")
        if action.action == "saving_throw":
            return self._execute_check_like(action, kind="saving_throw")
        if action.action == "damage_roll":
            return self._execute_damage_roll(action)
        if action.action == "raw_roll":
            return self._execute_raw_roll(action)
        raise RulesEngineError(f"unsupported action: {action.action}")

    def _execute_attack_roll(self, action: RuleAction) -> dict[str, object]:
        if action.target is None:
            raise RulesEngineError("attack_roll requires a target")

        if "attack_bonus" not in action.parameters:
            raise RulesEngineError("attack_roll requires attack_bonus")

        attack_bonus = int(action.parameters["attack_bonus"])
        advantage = str(action.parameters.get("advantage", "none"))
        attack_roll = self._roll(f"1d20+{attack_bonus}", advantage=advantage)
        damage_expression = str(action.parameters.get("damage_expression", "0"))
        damage_roll = self._roll(damage_expression) if attack_roll.total >= action.target.armor_class else None
        return {
            "action": "attack_roll",
            "actor": action.actor.name,
            "target": action.target.name,
            "weapon": action.parameters.get("weapon", "unarmed"),
            "roll": attack_roll.rendered,
            "attack_bonus": attack_bonus,
            "total": attack_roll.total,
            "damage": damage_roll.total if damage_roll else 0,
            "damage_roll": damage_roll.rendered if damage_roll else None,
            "advantage": advantage,
            "hit": attack_roll.total >= action.target.armor_class,
        }

    def _execute_check_like(self, action: RuleAction, *, kind: str) -> dict[str, object]:
        modifier = int(action.parameters.get("modifier", 0))
        advantage = str(action.parameters.get("advantage", "none"))
        label = str(action.parameters.get("label", kind))
        outcome = self._roll(f"1d20+{modifier}", advantage=advantage)
        return {
            "action": kind,
            "actor": action.actor.name,
            "label": label,
            "modifier": modifier,
            "advantage": advantage,
            "roll": outcome.rendered,
            "total": outcome.total,
        }

    def _execute_damage_roll(self, action: RuleAction) -> dict[str, object]:
        expression = str(action.parameters.get("damage_expression", ""))
        if not expression:
            raise RulesEngineError("damage_roll requires damage_expression")
        outcome = self._roll(expression)
        return {
            "action": "damage_roll",
            "actor": action.actor.name,
            "damage_type": str(action.parameters.get("damage_type", "untyped")),
            "roll": outcome.rendered,
            "total": outcome.total,
        }

    def _execute_raw_roll(self, action: RuleAction) -> dict[str, object]:
        expression = str(action.parameters.get("expression", ""))
        if not expression:
            raise RulesEngineError("raw_roll requires expression")
        outcome = self._roll(expression)
        return {
            "action": "raw_roll",
            "actor": action.actor.name,
            "roll": outcome.rendered,
            "total": outcome.total,
        }

    def _roll(self, expression: str, *, advantage: str = "none") -> DiceOutcome:
        try:
            return self._dice_roller.roll(expression, advantage=advantage)
        except Exception as exc:
            raise RulesEngineError(str(exc)) from exc


class _LegacyDiceRoller:
    def __init__(self, resolver: Callable[[str], int] | None) -> None:
        self._resolver = resolver or (lambda expr: 10)

    def roll(self, expression: str, *, advantage: str = "none") -> DiceOutcome:
        total = int(self._resolve_expression(expression))
        return DiceOutcome(
            expression=expression,
            total=total,
            rendered=f"{expression} = `{total}`",
        )

    def _resolve_expression(self, expression: str) -> int:
        if expression.startswith("1d20+") or expression.startswith("1d20-"):
            modifier = int(expression[4:])
            return int(self._resolver("1d20")) + modifier
        return int(self._resolver(expression))
