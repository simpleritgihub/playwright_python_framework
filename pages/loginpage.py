from pages.basepage import BasePage


class LoginPage(BasePage):
    username_input = "input[name='username']"
    password_input = "input[name='password']"
    login_button = "button[type='submit']"

    def login(self, username, password):
        self.page.locator(self.username_input).wait_for(state="visible")
        self.page.locator(self.password_input)

        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click_element(self.login_button)


from playwright.sync_api import Page