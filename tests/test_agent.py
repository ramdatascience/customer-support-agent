import pytest
from unittest.mock import patch, MagicMock


@patch("agents.support_agent.ChatOpenAI")
@patch("agents.support_agent.create_openai_tools_agent")
@patch("agents.support_agent.AgentExecutor")
def test_agent_chat_returns_output(mock_executor_cls, mock_create_agent, mock_llm_cls):
    mock_executor = MagicMock()
    mock_executor.invoke.return_value = {"output": "Ticket created successfully!"}
    mock_executor_cls.return_value = mock_executor

    from agents.support_agent import SupportAgent
    agent = SupportAgent()
    result = agent.chat("I can't log into my account.")

    assert "Ticket" in result or result != ""
    mock_executor.invoke.assert_called_once()


@patch("agents.support_agent.ChatOpenAI")
@patch("agents.support_agent.create_openai_tools_agent")
@patch("agents.support_agent.AgentExecutor")
def test_agent_handles_empty_output(mock_executor_cls, mock_create_agent, mock_llm_cls):
    mock_executor = MagicMock()
    mock_executor.invoke.return_value = {}
    mock_executor_cls.return_value = mock_executor

    from agents.support_agent import SupportAgent
    agent = SupportAgent()
    result = agent.chat("Hello")

    assert result == "I'm sorry, I couldn't process that."
