import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_btn_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_class_name('btn-add-to-basket')
    assert button, "No add to basket button"


