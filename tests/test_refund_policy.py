
from deepeval import assert_test
from deepeval.test_case import LLMTestCase

from utils.llm_client import get_llm_response
from utils.metrics import get_llm_metrics


REFUND_POLICY = (
    "Refunds are processed within 5 business days."
)


def test_refund_processing_time():

    question = "How long will my refund take?"

    expected_answer = (
        "Refunds are processed within 5 business days."
    )

    actual_answer = get_llm_response(question)

    test_case = LLMTestCase(
        input=question,
        actual_output=actual_answer,
        expected_output=expected_answer,
        context=[REFUND_POLICY]
    )

    assert_test(test_case, get_llm_metrics())


def test_refund_receiving_time():

    question = "When will I receive my refund?"

    expected_answer = (
        "Refunds are processed within 5 business days."
    )

    actual_answer = get_llm_response(question)

    test_case = LLMTestCase(
        input=question,
        actual_output=actual_answer,
        expected_output=expected_answer,
        context=[REFUND_POLICY]
    )

    assert_test(test_case, get_llm_metrics())


def test_refund_within_two_days():

    question = "Can I get my refund within 2 business days?"

    expected_answer = "I do not know."

    actual_answer = get_llm_response(question)

    test_case = LLMTestCase(
        input=question,
        actual_output=actual_answer,
        expected_output=expected_answer,
        context=[REFUND_POLICY]
    )

    assert_test(test_case, get_llm_metrics())


def test_refund_business_days():

    question = "How many business days does a refund take?"

    expected_answer = (
        "Refunds are processed within 5 business days."
    )

    actual_answer = get_llm_response(question)

    test_case = LLMTestCase(
        input=question,
        actual_output=actual_answer,
        expected_output=expected_answer,
        context=[REFUND_POLICY]
    )

    assert_test(test_case, get_llm_metrics())
