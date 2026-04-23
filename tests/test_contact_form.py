import allure
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.contact_form_page import ContactFormPage


@allure.suite("Contact Form")
class TestContactFormCaptcha:

    @allure.title("Contact form shows captcha error when submitted without captcha - company: {company}")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("name,email,company", [
        ("John Doe", "john.doe@example.com", "Assaia Test Corp"),
        ("Jane Smith", "jane.smith@airline.com", "Global Airlines"),
        ("Carlos García", "carlos@airport.es", "Aeropuerto Internacional"),
    ])
    def test_captcha_error_on_submit(self, page: Page, name: str, email: str, company: str):
        home = HomePage(page)
        home.open()
        home.accept_cookies()
        home.open_contact_form()

        contact = ContactFormPage(page)
        contact.fill_form(name=name, email=email, company=company)
        contact.submit()
        contact.assert_captcha_error_visible()
        contact.assert_form_not_submitted()