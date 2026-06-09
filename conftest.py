import pytest

@pytest.fixture(params=["chromium", "firefox", "webkit"])
def browser(playwright, request):
    browser = getattr(playwright, request.param).launch(headless=False)
    yield browser
    browser.close()