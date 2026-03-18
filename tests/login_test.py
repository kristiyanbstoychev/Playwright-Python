from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import os

def test_succesfull_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.fill_login_form(os.getenv("USERNAME", ""), os.getenv("PASSWORD", ""))