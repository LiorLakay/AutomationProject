import pytest
from config import CONFIG
from pom.registration_page import RegistrationPage
from pom.login_page import LoginPage

def test_registration(browser_context):
    try:
        registration_page = RegistrationPage(browser_context)
        registration_page.pre_registration_signup(CONFIG["new_user"]["username"], CONFIG["new_user"]["email"])

        if registration_page.is_email_already_in_use():
            raise Exception("Email has already been registered. Try to use different email address")

        registration_page.register(
            CONFIG["new_user"]["password"],
            CONFIG["new_user"]["first_name"],
            CONFIG["new_user"]["last_name"],
            CONFIG["new_user"]["address"],
            CONFIG["new_user"]["country"],
            CONFIG["new_user"]["city"],
            CONFIG["new_user"]["zipcode"],
            CONFIG["new_user"]["mobile_number"]
        )

        assert registration_page.is_registration_successful(), "Something in the registration process gone wrong"

    except Exception as e:
        pytest.fail(f"Test failed: {e}")


def test_login(browser_context):
    try:
        login_page = LoginPage(browser_context)
        login_page.login_user(CONFIG["new_user"]["email"], CONFIG["new_user"]["password"])

        assert login_page.is_login_successful(), "Something in the login process gone wrong"

    except Exception as e:
        pytest.fail(f"Test failed: {e}")

