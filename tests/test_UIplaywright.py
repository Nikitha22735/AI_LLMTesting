import allure
from playwright.sync_api import sync_playwright, expect
# p = sync_playwright().start()
def test_UITesting1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width":1000,"height":500})
        page = context.new_page()
        try:
            page.goto("http://localhost:8501/")
            page.wait_for_timeout(5000)
            edText = page.get_by_text('Education123 Assistant')
            expect(edText).to_be_visible()
            expect(page.get_by_test_id("stSidebarUserContent").get_by_text("Education")).to_be_visible()
            expect(page.get_by_test_id("stSidebarUserContent").get_by_test_id("stBaseButton-secondary")).to_be_visible()
        except Exception:
            allure.attach(
                page.screenshot(),
                name="failedstep",
                attachment_type=allure.attachment_type.PNG
            )
            raise

# p.stop()

def test_UITesting2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width":1000,"height":500})
        page = context.new_page()
        page.goto("http://localhost:8501/")
        expect(page.get_by_test_id("stChatInputTextArea")).to_be_visible()
        page.wait_for_timeout(5000)


def test_UITesting3(page):
    page.goto("http://localhost:8501/")

    chat_input = page.get_by_test_id("stChatInputTextArea")
    expect(chat_input).to_be_visible()

    chat_messages = page.get_by_test_id("stChatMessage")
    previous_message_count = chat_messages.count()

    chat_input.fill("what is Testing")
    chat_input.press("Enter")

    expect(chat_messages).to_have_count(previous_message_count + 2, timeout=60000)
    response_text = chat_messages.last.inner_text().strip()
    assert "testing" in response_text.lower(), (
        f"Expected the assistant response to mention Testing, got: {response_text}"
    )



