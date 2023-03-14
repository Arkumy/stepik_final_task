from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: es or fr")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(25.0)
    yield browser
    browser.quit()
