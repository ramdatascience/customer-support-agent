import json
import os
from typing import Optional
from models.ticket import Ticket, TicketStatus
from utils.logger import get_logger

logger = get_logger(__name__)
STORAGE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "tickets.json")


class TicketStore:
    """Handles persistence of support tickets to a local JSON file."""

    def __init__(self, path: str = STORAGE_PATH):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            self._write([])

    def _read(self) -> list[dict]:
        with open(self.path, "r") as f:
            return json.load(f)

    def _write(self, data: list[dict]):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def save_ticket(self, ticket: Ticket) -> Ticket:
        tickets = self._read()
        tickets.append(ticket.model_dump())
        self._write(tickets)
        logger.info(f"Ticket {ticket.ticket_id} saved successfully.")
        return ticket

    def get_ticket(self, ticket_id: str) -> Optional[Ticket]:
        tickets = self._read()
        for t in tickets:
            if t["ticket_id"] == ticket_id:
                return Ticket(**t)
        return None

    def update_status(self, ticket_id: str, status: TicketStatus) -> Optional[Ticket]:
        tickets = self._read()
        for t in tickets:
            if t["ticket_id"] == ticket_id:
                t["status"] = status.value
                self._write(tickets)
                logger.info(f"Ticket {ticket_id} status updated to {status.value}.")
                return Ticket(**t)
        return None

    def list_tickets(self) -> list[Ticket]:
        return [Ticket(**t) for t in self._read()]
