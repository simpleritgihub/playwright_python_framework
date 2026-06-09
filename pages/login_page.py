from playwright.sync_api import Pageimport pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="session",params=["chrome","firefox","safari"])
def test_login(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        title = page.title()
        print("The title:", title)

        assert "OrangeHRMa" in title
        yield browser
        page.wait_for_timeout(4000)

        browser.close()