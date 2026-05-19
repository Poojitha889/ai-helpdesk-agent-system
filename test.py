import os
from dotenv import load_dotenv

import vertexai
from vertexai.generative_models import GenerativeModel

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION
)

model = GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Hello")

print(response.text)