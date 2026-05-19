import os
from dotenv import load_dotenv

import vertexai
from vertexai.generative_models import GenerativeModel
from vertexai.generative_models import GenerationConfig

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION
)

model = GenerativeModel("gemini-2.5-flash")


def classify_issue(issue):

    prompt = f"""
Classify the IT issue.

Return ONLY:

Category: <category>
Priority: <priority>

Allowed Categories:
Network
Hardware
Software
Security
Access

Allowed Priorities:
Low
Medium
High

Issue:
{issue}
"""

    response = model.generate_content(
        prompt,
        generation_config=GenerationConfig(
            temperature=0,
            max_output_tokens=30
        )
    )

    return response.text.strip()