from __future__ import annotations
import pytest
from pytest_bdd import given, when, then, scenarios

scenarios("../features/combat_round.feature")


@given("a campaign session with 3 ready players in SCENE_ROUND_OPEN")
def a_session():
    pytest.skip("Step definitions for BDD scaffold — implement as needed")


@then("the rules engine resolves each action in initiative order")
def rules_resolve():
    pytest.skip("Step definitions for BDD scaffold — implement as needed")
