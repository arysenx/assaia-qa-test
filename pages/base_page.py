import allure
from playwright.sync_api import Page, expect


class BasePage:
    """Base class for all Page Objects. Contains shared navigation and utility methods."""

    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url

    @allure.step("Navigate to {url}")
    def navigate(self, url: str = "") -> None:
        target = url or self.base_url
        self.page.goto(target)

    @allure.step("Get page title")
    def get_title(self) -> str:
        return self.page.title()

    @allure.step("Wait for element: {selector}")
    def wait_for_element(self, selector: str, timeout: int = 10_000):
        return self.page.wait_for_selector(selector, timeout=timeout)

    @allure.step("Click element: {selector}")
    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    @allure.step("Fill field: {selector}")
    def fill(self, selector: str, value: str) -> None:
        self.page.locator(selector).fill(value)

    @allure.step("Get text of element: {selector}")
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    @allure.step("Assert element is visible: {selector}")
    def assert_visible(self, selector: str) -> None:
        expect(self.page.locator(selector)).to_be_visible()

    @allure.step("Assert URL contains: {partial_url}")
    def assert_url_contains(self, partial_url: str) -> None:
        expect(self.page).to_have_url(f".*{partial_url}.*")

    @allure.step("Take screenshot")
    def screenshot(self, name: str = "screenshot") -> None:
        allure.attach(
            self.page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )
