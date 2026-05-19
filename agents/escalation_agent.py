def check_escalation(priority, issue):

    high_priority_keywords = [
        "server down",
        "data breach",
        "phishing",
        "ransomware",
        "production issue",
        "system outage",
        "security attack"
    ]

    issue_lower = issue.lower()

    if priority == "High":
        return "Escalate to Level 2 Support Team"

    for keyword in high_priority_keywords:

        if keyword in issue_lower:
            return "Escalate to Security/Infrastructure Team"

    return "No Escalation Required"