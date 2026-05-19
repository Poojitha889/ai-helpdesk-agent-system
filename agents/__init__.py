from agents.classifier_agent import classify_issue
from agents.troubleshooting_agent import troubleshoot_issue

from tools.ticket_tools import create_ticket


def process_issue(issue):

    classification = classify_issue(issue)

    category = "General"
    priority = "Medium"

    lines = classification.split("\n")

    for line in lines:

        if "Category" in line:
            category = line.split(":")[-1].strip()

        if "Priority" in line:
            priority = line.split(":")[-1].strip()

    ticket = create_ticket(
        issue,
        category,
        priority
    )

    troubleshooting = troubleshoot_issue(issue)

    return {
        "ticket": ticket,
        "classification": classification,
        "troubleshooting": troubleshooting
    }