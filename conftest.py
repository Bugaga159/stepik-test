import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default=None, help='Choose browser: ru or en or es')

@pytest.fixture(scope="function")
def browser(request):
    option = Options()
    language = request.config.getoption('language')
    option.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=option)
    else:
        print('Error, you not choose browser chrome!')
    yield browser
    print("\nquit browser..")
    browser.quit()
