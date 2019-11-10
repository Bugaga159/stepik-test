import time
import math
from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def answer():
    return math.log(int(time.time()))

numberArr = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']
textError = []
@pytest.mark.parametrize('number', numberArr)
def test_ansver_take(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)

    textBtn1 = browser.find_element_by_css_selector('textarea')

    print(answer())
    textBtn1.send_keys(str(answer()))

    button = browser.find_element_by_xpath('//*/button[@class="submit-submission"]')

    button.click()
    textOutput = browser.find_element_by_xpath('//*/pre[@class="smart-hints__hint"]').text

    if textOutput != 'Correct!':
        textError.append(textOutput)
        print("".join(textError))
        assert False, f'Не прошел тест - {number}'
    else:
        print(textError)
        assert True
