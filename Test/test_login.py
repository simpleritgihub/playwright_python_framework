import time
from pages.loginpage import LoginPage
from utilities.configreader import ConfigReader


def test_login(page):
    page.goto(ConfigReader.QA_URL)

    login_page = LoginPage(page)

    login_page.login(
        ConfigReader.USERNAME,
        ConfigReader.PASSWORD
    )

    page.wait_for_timeout(4000)