import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def pytest_addoption(parser):
    parser.addoption("--language", action="store", default='en-gb', help="Specify the language for the tests")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    print("\nquit browser..")
    browser.quit()
