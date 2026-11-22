
import pytest

from utils.llm_client import get_llm_response
from utils.metrics import get_llm_metrics


@pytest.fixture
def llm_response():

    return get_llm_response


@pytest.fixture
def llm_metrics():

    return get_llm_metrics
