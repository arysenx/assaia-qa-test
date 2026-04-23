import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ContactFormPage(BasePage):
    """Page Object for the Assaia 'Get in touch' contact form."""

    # Locators
    GET_IN_TOUCH_BUTTON = "text=Get in touch"
    NAME_INPUT = "#name"
    EMAIL_INPUT = "#email"
    COMPANY_INPUT = "#Company"
    SUBMIT_BUTTON = "[name='submit']"
    CAPTCHA_ERROR = ".g-recaptcha-error"

    def __init__(self, page: Page, base_url: str = "https://www.assaia.com/"):
        super().__init__(page, base_url)

    @allure.step("Fill contact form")
    def fill_form(self, name: str, email: str, company: str) -> "ContactFormPage":
        self.fill(self.NAME_INPUT, name)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.COMPANY_INPUT, company)
        return self

    @allure.step("Click submit button")
    def submit(self) -> "ContactFormPage":
        self.click(self.SUBMIT_BUTTON)
        return self

    @allure.step("Assert captcha error is present")
    def assert_captcha_error_visible(self) -> None:
        self.page.wait_for_selector(self.CAPTCHA_ERROR, state="attached", timeout=5000)
        expect(self.page.locator(self.CAPTCHA_ERROR).first).to_be_attached()
        self.screenshot("captcha_error")

    @allure.step("Assert form was not submitted")
    def assert_form_not_submitted(self) -> None:
        self.assert_visible(".modal_cta.is-visible")