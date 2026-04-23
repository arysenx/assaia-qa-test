import pytest
from playwright.sync_api import Browser


@pytest.fixture(scope="session")
def browser_instance():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        yield browser
        browser.close()


@pytest.fixture
def page(browser_instance: Browser):
    context = browser_instance.new_context(
        viewport={"width": 1920, "height": 1080},
        locale="en-US",
    )
    page = context.new_page()
    yield page
    context.close()