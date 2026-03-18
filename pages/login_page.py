from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.get_by_test_id("username")
        self.password_input = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-button")

    def fill_login_form(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)