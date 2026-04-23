import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object for the Assaia homepage."""

    # Locators
    COOKIE_ACCEPT_BTN = "#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"

    def __init__(self, page: Page, base_url: str = "https://www.assaia.com/"):
        super().__init__(page, base_url)

    @allure.step("Open Assaia homepage")
    def open(self) -> "HomePage":
        self.navigate(self.base_url)
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        return self

    @allure.step("Accept cookies")
    def accept_cookies(self) -> "HomePage":
        try:
            self.page.wait_for_selector(self.COOKIE_ACCEPT_BTN, timeout=5000)
            self.click(self.COOKIE_ACCEPT_BTN)
        except Exception:
            pass
        return self

    @allure.step("Click 'Get in touch' button")
    def open_contact_form(self) -> "HomePage":
        self.page.evaluate("document.querySelector(\"a[call-cta='true']\").click()")
        self.page.wait_for_selector(".modal_cta.is-visible", state="visible")
        return self