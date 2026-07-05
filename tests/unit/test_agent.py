"""Data Governance Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_catalog_dataset():
    """Test Register a dataset in the data catalog with metadata."""
    tools = AgentTools()
    result = await tools.catalog_dataset(dataset="test", owner="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_classify_data():
    """Test Classify data sensitivity level (public, internal, confidential, restricted)."""
    tools = AgentTools()
    result = await tools.classify_data(dataset="test", scan_columns=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_set_access_policy():
    """Test Set access policy for a dataset based on classification."""
    tools = AgentTools()
    result = await tools.set_access_policy(dataset="test", policy="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_ownership():
    """Test Assign or transfer data ownership and stewardship."""
    tools = AgentTools()
    result = await tools.track_ownership(dataset="test", owner="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.data_governance_agent_agent import DataGovernanceAgentAgent
    agent = DataGovernanceAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
