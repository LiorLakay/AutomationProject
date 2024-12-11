from config import CONFIG
from playwright.sync_api import Page


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = "input[name='name']"
        self.email = "[data-qa='signup-email']"
        self.signup = 'button[type="submit"]:has-text("Signup")'
        self.gender_title = "#id_gender1"
        self.password = "#password"
        self.first_name = "#first_name"
        self.last_name = "#last_name"
        self.address = "#address1"
        self.country_dropdown = "#country"
        self.state = "#state"
        self.city = "#city"
        self.zipcode = "#zipcode"
        self.mobile_number = "#mobile_number"
        self.submit = "Create Account"

    def pre_registration_signup(self, username, email):
        self.navigate_to_pre_registration_page(CONFIG["app_url"])
        self.page.fill(self.username, username)
        self.page.fill(self.email, email)
        self.page.click(self.signup)


    def navigate_to_pre_registration_page(self, base_url):
        if base_url.endswith("/"):
            self.page.goto(base_url + "login")
        else:
            self.page.goto(base_url + "/login")


    def register(self, password, first_name, last_name, address, country, city, zipcode, mobile_num):
        self.page.click(self.gender_title)
        self.page.fill(self.password, password)
        self.page.fill(self.first_name, first_name)
        self.page.fill(self.last_name, last_name)
        self.page.fill(self.address, address)
        self.page.select_option(self.country_dropdown, value=country)
        self.page.fill(self.state, country)
        self.page.fill(self.city, city)
        self.page.fill(self.zipcode, zipcode)
        self.page.fill(self.mobile_number, mobile_num)
        self.page.click(f"text={self.submit}")

    def is_registration_successful(self):
        return self.page.is_visible('text="Account Created!"')

    def is_email_already_in_use(self):
        return self.page.is_visible('text="Email Address already exist!"')
