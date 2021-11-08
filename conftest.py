import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="write language")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    browser = webdriver.Chrome()
    print(f"\nstart browser for test with language:{language_name}..")
    yield browser
    print("\nquit browser..")
    browser.quit()
    
    
