import pytest
from unittest.mock import patch, MagicMock
from models.ticket import Ticket, TicketPriority, TicketStatus


def make_ticket(**kwargs):
    defaults = dict(customer_name="John Doe", customer_email="john@example.com", issue="Login not working")
    defaults.update(kwargs)
    return Ticket(**defaults)


def test_ticket_creation():
    ticket = make_ticket()
    assert ticket.status == TicketStatus.OPEN
    assert ticket.priority == TicketPriority.MEDIUM
    assert len(ticket.ticket_id) == 8


def test_ticket_to_summary():
    ticket = make_ticket()
    summary = ticket.to_summary()
    assert "John Doe" in summary
    assert "john@example.com" in summary
    assert "Login not working" in summary


def test_ticket_high_priority():
    ticket = make_ticket(priority=TicketPriority.HIGH)
    assert ticket.priority == TicketPriority.HIGH


def test_ticket_id_uniqueness():
    tickets = [make_ticket() for _ in range(10)]
    ids = [t.ticket_id for t in tickets]
    assert len(set(ids)) == 10
