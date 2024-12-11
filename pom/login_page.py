from config import CONFIG
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = "[data-qa='login-email']"
        self.password = "input[name='password']"
        self.login = 'button[type="submit"]:has-text("Login")'

    def navigate_to_login_page(self, base_url):
        if base_url.endswith("/"):
            self.page.goto(base_url + "login")
        else:
            self.page.goto(base_url + "/login")

    def login_user(self, email, password):
        self.navigate_to_login_page(CONFIG["app_url"])
        self.page.fill(self.email, email)
        self.page.fill(self.password, password)
        self.page.click(self.login)

    def is_login_successful(self):
        return self.page.is_visible('a:text("Logout")')
