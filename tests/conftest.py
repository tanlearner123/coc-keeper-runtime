"""Shared pytest fixtures for Track E scenario tests."""

from __future__ import annotations
import pytest
import vcr
from pathlib import Path
from dm_bot.persistence.store import PersistenceStore


@pytest.fixture
def interaction_factory():
    from tests.fakes.discord import fake_interaction

    return fake_interaction


@pytest.fixture
def context_factory():
    from tests.fakes.discord import fake_context

    return fake_context


@pytest.fixture
def sqlite_memory_store():
    return PersistenceStore(Path("file::memory:?cache=shared"))


@pytest.fixture
def sqlite_memory_path(tmp_path):
    return tmp_path / "test.db"


@pytest.fixture
def fast_model_mock():
    from tests.fakes.models import FastMock

    return FastMock()


@pytest.fixture
def slow_model_mock():
    from tests.fakes.models import SlowMock

    return SlowMock(delay_seconds=0.1)


@pytest.fixture
def error_model_mock():
    from tests.fakes.models import ErrorMock

    return ErrorMock()


@pytest.fixture(scope="session")
def vcr_config():
    return {
        "record_mode": "once",
        "filter_headers": [("authorization", "REDACTED")],
        "cassette_library_dir": "tests/cassettes",
    }
