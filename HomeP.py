class HomePage():

    def __init__(self,driver):
        self.driver = driver
        self.email_textbox_xpath ="//input[@id='email']"
        self.sign_up_xpath ="//img[@id='enterimg']"


    def click_sign_up(self):
        self.driver.find_element_by_xpath(self.sign_up_xpath).click()