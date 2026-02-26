from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
import uuid


class TicketPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TicketStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class Ticket(BaseModel):
    ticket_id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8].upper())
    customer_name: str
    customer_email: str
    issue: str
    priority: TicketPriority = TicketPriority.MEDIUM
    status: TicketStatus = TicketStatus.OPEN
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now().isoformat())

    def to_summary(self) -> str:
        return (
            f"Ticket ID: {self.ticket_id}\n"
            f"Customer: {self.customer_name} ({self.customer_email})\n"
            f"Issue: {self.issue}\n"
            f"Priority: {self.priority.value.upper()}\n"
            f"Status: {self.status.value.upper()}\n"
            f"Created: {self.created_at}"
        )
