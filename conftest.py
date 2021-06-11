import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")
                     
@pytest.fixture(scope="function")
def browser(request):
    user_lang = request.config.getoption("language")
    if user_lang:
        print("\nstart chrome browser for test..")
        
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)

        yield browser

    else:
        raise pytest.UsageError("--pls choose language")

    print("\nquit browser..")
    browser.quit()
  
