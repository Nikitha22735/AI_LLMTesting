
import os
from dotenv import load_dotenv

from deepeval.models import OpenAIModel

from deepeval.metrics import (
    AnswerRelevancyMetric,
    HallucinationMetric,
    ExactMatchMetric
)

load_dotenv()

PROJECT_ENDPOINT = os.environ["FOUNDRY_ENDPOINT"].rstrip("/")
API_KEY = os.environ["FOUNDRY_API_KEY"]

MODEL_DEPLOYMENT = "gpt-4o"

BASE_URL = f"{PROJECT_ENDPOINT}/openai/v1/"


def get_judge_model():

    return OpenAIModel(
        model=MODEL_DEPLOYMENT,
        base_url=BASE_URL,
        api_key=API_KEY,
        temperature=0
    )


def get_llm_metrics():

    judge_model = get_judge_model()

    relevancy = AnswerRelevancyMetric(
        threshold=0.7,
        model=judge_model,
        include_reason=True
    )

    correctness = ExactMatchMetric(
        threshold=1.0
    )

    hallucination = HallucinationMetric(
        threshold=0.7,
        model=judge_model,
        include_reason=True
    )

    return [
        relevancy,
        correctness,
        hallucination
    ]
