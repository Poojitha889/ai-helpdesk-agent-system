from tools.ticket_tools import create_ticket


def process_issue(issue):

    ticket = create_ticket(
        issue,
        "Network",
        "Medium"
    )

    return {
        "ticket": ticket,
        "classification": "Category: Network\nPriority: Medium",
        "troubleshooting": "1. Restart VPN\n2. Clear credentials\n3. Re-enter password",
        "escalation": "No Escalation Required",
        "asset_info": {
            "employee": "John",
            "device": "Dell Laptop"
        }
    }