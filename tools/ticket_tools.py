from langchain.tools import tool
from models.ticket import Ticket, TicketPriority, TicketStatus
from storage.ticket_store import TicketStore

store = TicketStore()


@tool
def create_ticket(customer_name: str, customer_email: str, issue: str, priority: str = "medium") -> str:
    """
    Creates a new support ticket for a customer issue.

    Args:
        customer_name: Full name of the customer.
        customer_email: Email address of the customer.
        issue: Description of the problem the customer is facing.
        priority: Priority level — 'low', 'medium', or 'high'. Defaults to 'medium'.

    Returns:
        A confirmation string with the ticket summary.
    """
    try:
        prio = TicketPriority(priority.lower())
    except ValueError:
        prio = TicketPriority.MEDIUM

    ticket = Ticket(
        customer_name=customer_name,
        customer_email=customer_email,
        issue=issue,
        priority=prio,
    )
    store.save_ticket(ticket)
    return f"✅ Ticket created successfully!\n\n{ticket.to_summary()}"


@tool
def get_ticket_status(ticket_id: str) -> str:
    """
    Retrieves the current status of a support ticket by its ID.

    Args:
        ticket_id: The unique ticket ID (e.g., 'A1B2C3D4').

    Returns:
        Ticket details or a not-found message.
    """
    ticket = store.get_ticket(ticket_id.upper())
    if ticket:
        return ticket.to_summary()
    return f"❌ No ticket found with ID: {ticket_id}"


@tool
def list_all_tickets() -> str:
    """
    Lists all support tickets in the system.

    Returns:
        A formatted list of all tickets.
    """
    tickets = store.list_tickets()
    if not tickets:
        return "No tickets found in the system."
    return "\n\n---\n\n".join(t.to_summary() for t in tickets)


@tool
def close_ticket(ticket_id: str) -> str:
    """
    Closes a support ticket by marking its status as 'closed'.

    Args:
        ticket_id: The unique ticket ID to close.

    Returns:
        Confirmation message.
    """
    ticket = store.update_status(ticket_id.upper(), TicketStatus.CLOSED)
    if ticket:
        return f"✅ Ticket {ticket_id} has been closed.\n\n{ticket.to_summary()}"
    return f"❌ No ticket found with ID: {ticket_id}"
