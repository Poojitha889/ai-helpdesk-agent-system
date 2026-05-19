import uuid
from datetime import datetime

tickets = []

def create_ticket(issue, category, priority):

    ticket = {
        "ticket_id": str(uuid.uuid4())[:8],
        "issue": issue,
        "category": category,
        "priority": priority,
        "status": "Open",
        "created_at": str(datetime.now())
    }

    tickets.append(ticket)

    return ticket