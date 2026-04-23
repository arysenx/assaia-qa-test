# Assaia QA Automation – Contact Form Test Suite

End-to-end test suite built with **Python 3.11 + Pytest + Playwright + Allure**.

---

## Stack

| Tool | Purpose |
|------|---------|
| Python 3.11+ | Language |
| Pytest | Test runner |
| Playwright (Chromium) | Browser automation |
| Allure | Reporting |
| uv | Dependency management |

---

## Setup

### 1. Install uv (if not installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Install Chromium

```bash
uv run playwright install chromium
```

---

## Run tests

```bash
# Run all tests
uv run pytest

# Run with visible browser
uv run pytest --headed

# Run a specific parametrize case
uv run pytest -k "John"
```

---

## Generate Allure report

```bash
allure serve allure-results
```

---

## Project structure
assaia-qa-test/
├── conftest.py              # Shared fixtures (browser, page)
├── pytest.ini               # Pytest + Allure config
├── pyproject.toml           # uv dependencies
├── pages/
│   ├── base_page.py         # Base Page Object (shared methods)
│   ├── home_page.py         # Homepage POM (cookies, navigation)
│   └── contact_form_page.py # Contact form POM
└── tests/
└── test_contact_form.py # Parametrized captcha validation tests

---

## Test scenario

**Contact Form Captcha Validation**

Verifies that the "Get in touch" form on [assaia.com](https://www.assaia.com/) does not submit when the captcha is not completed.

Steps:
1. Navigate to the homepage
2. Accept cookies
3. Open the "Get in touch" modal
4. Fill in Name, Email and Company fields
5. Click Submit without completing the captcha
6. Assert that a captcha error is present in the DOM

The test is parametrized with 3 different sets of input data:

| Name | Email | Company |
|------|-------|---------|
| John Doe | john.doe@example.com | Assaia Test Corp |
| Jane Smith | jane.smith@airline.com | Global Airlines |
| Carlos García | carlos@airport.es | Aeropuerto Internacional |

---

## Design decisions

- **Page Object Model** — selectors and interactions encapsulated in page classes, tests only call high-level methods
- **Allure steps** — every page method decorated with `@allure.step` for full traceability
- **Screenshots** — captured and attached to Allure on key assertions
- **Session-scoped browser** — single browser instance per test session for performance
- **Function-scoped page** — fresh page context per test for isolation