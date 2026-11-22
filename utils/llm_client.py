
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.environ["FOUNDRY_ENDPOINT"].rstrip("/")
API_KEY = os.environ["FOUNDRY_API_KEY"]

MODEL_DEPLOYMENT = "gpt-4o"

client = OpenAI(
    base_url=f"{PROJECT_ENDPOINT}/openai/v1/",
    api_key=API_KEY
)

SYSTEM_PROMPT = """
You are a customer-support chatbot.

Answer only using this refund policy:
Refunds are processed within 5 business days.

If the answer is not in the policy,
say you do not know.
"""

def get_llm_response(question):

    response = client.responses.create(
        model=MODEL_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=question
    )

    return response.output_text.strip()
