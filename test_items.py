from selenium.common.exceptions import NoSuchElementException
import time

def test_guest_should_see_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #Если нужно проверить визуально, снять коммит с time
    time.sleep(30)
    try:
        btn_add = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
        assert btn_add
    except NoSuchElementException:
        print('Button not found!')
        assert False
