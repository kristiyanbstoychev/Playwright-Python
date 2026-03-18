import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, Playwright

load_dotenv()

@pytest.fixture(scope="session", autouse=True)
def set_test_id_attribute(playwright: Playwright):
    playwright.selectors.set_test_id_attribute(
        os.getenv("TEST_ID_ATTRIBUTE", "")
    )

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "base_url": os.getenv("BASE_URL", "")
    }

@pytest.fixture(autouse=True)
def navigate_to_home(page: Page):
    page.goto("/")