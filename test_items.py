def test_button_should_be_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(button) > 0, "Button is not present"