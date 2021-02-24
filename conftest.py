import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# добавляем опцию --language в pytest
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: en-gb, es, fr, ru, uk, it, de, pt and others')


@pytest.fixture(scope='function')
def browser(request) -> webdriver:
    lang = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe',options=options)
    browser.maximize_window()
    yield browser
    browser.quit()