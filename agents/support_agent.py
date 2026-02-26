from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from tools.ticket_tools import create_ticket, get_ticket_status, list_all_tickets, close_ticket
from utils.logger import get_logger
import os

logger = get_logger(__name__)

SYSTEM_PROMPT = """You are a professional and empathetic customer support agent for TechCorp.
Your job is to help customers by creating, tracking, and managing their support tickets.

You have access to the following tools:
- create_ticket: Create a new ticket when a customer reports an issue.
- get_ticket_status: Check the status of an existing ticket.
- list_all_tickets: List all support tickets (admin use).
- close_ticket: Close a resolved ticket.

Guidelines:
- Always greet the customer warmly.
- If a customer describes a problem, proactively collect their name and email and create a ticket.
- If the customer provides a ticket ID, check the status.
- Be concise, professional, and solution-focused.
- If you cannot help, politely explain the limitation.
"""


class SupportAgent:
    """Agentic customer support system powered by LangChain + OpenAI."""

    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
            temperature=float(os.getenv("TEMPERATURE", 0.3)),
        )
        self.tools = [create_ticket, get_ticket_status, list_all_tickets, close_ticket]
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.agent_executor = self._build_agent()

    def _build_agent(self) -> AgentExecutor:
        prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        agent = create_openai_tools_agent(self.llm, self.tools, prompt)
        return AgentExecutor(
            agent=agent,
            tools=self.tools,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True,
        )

    def chat(self, user_input: str) -> str:
        logger.info(f"User: {user_input}")
        response = self.agent_executor.invoke({"input": user_input})
        output = response.get("output", "I'm sorry, I couldn't process that.")
        logger.info(f"Agent: {output}")
        return output
