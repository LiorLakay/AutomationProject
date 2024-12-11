from playwright.sync_api import sync_playwright
import pytest

from network_handlers import handle_network_errors


@pytest.fixture(scope="session")
def setup_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="function")
def browser_context(setup_playwright):
    browser = setup_playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    handle_network_errors(page)
    yield page
    context.close()
    browser.close()
