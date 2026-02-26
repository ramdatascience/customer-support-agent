# 🤖 Customer Support Agent — Agentic AI System

> An intelligent, agentic customer support system built with **LangChain**, **OpenAI GPT**, and **Python**. The agent autonomously handles customer ticket creation, status tracking, and ticket management through natural conversation.

---

## 🧠 Architecture

```
User Input → LangChain Agent (OpenAI Tools) → Tool Selection → JSON Storage
                      ↑
             ConversationBufferMemory (multi-turn context)
```

The system follows a modular design with clear separation of concerns:

| Layer | Responsibility |
|---|---|
| `agents/` | LangChain agent setup & execution |
| `tools/` | LangChain tool definitions (actions the agent can take) |
| `models/` | Pydantic data models (Ticket schema) |
| `storage/` | JSON-based ticket persistence layer |
| `utils/` | Logging utilities |

---

## ✨ Features

- 🎫 **Ticket Creation** — Agent extracts customer name, email, issue, and priority from conversation and creates a ticket
- 🔍 **Status Lookup** — Retrieve any ticket by its ID
- 📋 **List All Tickets** — Admin view of all open/closed tickets
- ✅ **Close Tickets** — Mark resolved tickets as closed
- 💬 **Multi-turn Memory** — Agent remembers conversation context
- 🧩 **Modular Design** — Easy to extend with new tools

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/customer-support-agent.git
cd customer-support-agent
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 5. Run the agent
```bash
python main.py
```

---

## 💬 Example Conversation

```
You: Hi, I'm having trouble with my account login. My name is Sarah and email is sarah@example.com.

Agent: Hello Sarah! I'm sorry to hear you're having trouble logging in. Let me create a support
       ticket for you right away.

       ✅ Ticket created successfully!

       Ticket ID: 4F9A2B1C
       Customer: Sarah (sarah@example.com)
       Issue: Trouble with account login
       Priority: MEDIUM
       Status: OPEN

You: Can you check ticket 4F9A2B1C?

Agent: Here are the details for that ticket:

       Ticket ID: 4F9A2B1C
       Status: OPEN
       ...
```

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 🛠 Tech Stack

- **Python 3.11+**
- **LangChain** — Agent framework & tool orchestration
- **OpenAI GPT-4o-mini** — LLM backbone
- **Pydantic v2** — Data validation & modeling
- **Rich** — Beautiful terminal UI
- **Pytest** — Unit testing

---

## 📂 Project Structure

```
customer-support-agent/
├── agents/          # LangChain agent definition
├── tools/           # LangChain tools (ticket actions)
├── models/          # Pydantic models
├── storage/         # JSON persistence layer
├── utils/           # Logger utility
├── data/            # tickets.json (auto-created)
├── tests/           # Unit tests
├── main.py          # Entry point
└── requirements.txt
```

---

## 🔮 Future Enhancements

- [ ] Add vector database (FAISS/Chroma) for semantic FAQ search
- [ ] Integrate email notifications on ticket creation
- [ ] Add a REST API layer with FastAPI
- [ ] Implement escalation logic for high-priority tickets
- [ ] Add a web UI with Streamlit

---

## 📄 License

MIT License © 2024

---

> Built to demonstrate agentic AI design patterns with LangChain and OpenAI tool-calling.
