class BasePage:

    def __init__(self, page):
        self.page = page

    def enter_text(self, locator, text):
        self.page.locator(locator).fill(text)

    def click_element(self, locator):
        self.page.locator(locator).click()

    def get_text(self, locator):
        return self.page.locator(locator).text_content()