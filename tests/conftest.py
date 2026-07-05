"""Test configuration for Data Governance Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "data-governance-agent", "category": "Data Engineering"}
