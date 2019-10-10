class OrderPage():

    def __init__(self, driver):
        self.driver = driver
        self.practice_page_xpath = "//a[contains(text(),'Practice Site')]"
        self.item_add_cart_xpath = "//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart']"
        self.cart_xpath = "//a[contains(@class,'added_to_cart wc-forward')]"
        self.proceed_to_chkout_xpath="//a[@class='checkout-button button alt wc-forward']"
        self.firstname_textbox_xpath="//input[@id='billing_first_name']"
        self.lastname_textbox_xpath="//input[@id='billing_last_name']"
        self.companyname_textbox_xpath="//input[@id='billing_company']"
        self.email_textbox_xpath="//input[@id='billing_email']"
        self.phone_textbox_xpath="//input[@id='billing_phone']"
        self.country_drpdwn_xpath="//span[@id='select2-chosen-1']"
        self.country_search_xpath="//input[@id='s2id_autogen1_search']"
        self.canada_xpath="//span[@class='select2-match']"
        self.adress_xpath="//input[@id='billing_address_1']"
        self.city_xpath="//input[@id='billing_city']"
        self.province_xpath="//div[@id='s2id_billing_state']//b"
        self.province_search_xpath="//input[@id='s2id_autogen2_search']"
        self.ontario_xpath="//span[@class='select2-match']"
        self.postalcode_xpath="//input[@id='billing_postcode']"
        self.cash_on_delivery_xpath="//input[@id='payment_method_cod']"
        self.place_order_xpath="//input[@id='place_order']"
    def click_practice_page(self):
        self.driver.find_element_by_xpath(self.practice_page_xpath).click()
    def click_add_to_cart(self):
        self.driver.find_element_by_xpath(self.item_add_cart_xpath).click()
    def click_cart(self):
        self.driver.find_element_by_xpath(self.cart_xpath).click()
    def click_checkout(self):
        self.driver.find_element_by_xpath(self.proceed_to_chkout_xpath).click()
    def enter_firstname(self,firstname):
        self.driver.find_element_by_xpath(self.firstname_textbox_xpath).send_keys(firstname)
    def enter_lastname(self,lastname):
        self.driver.find_element_by_xpath(self.lastname_textbox_xpath).send_keys(lastname)
    def enter_company_name(self,company):
        self.driver.find_element_by_xpath(self.companyname_textbox_xpath).send_keys(company)
    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)
    def enter_phone(self,phone):
        self.driver.find_element_by_xpath(self.phone_textbox_xpath).send_keys(phone)
    def select_country(self):
        self.driver.find_element_by_xpath(self.country_drpdwn_xpath).click()
        self.driver.find_element_by_xpath(self.country_search_xpath).send_keys("Canada")
        self.driver.find_element_by_xpath(self.canada_xpath).click()
    def enter_adress(self,adress):
        self.driver.find_element_by_xpath(self.adress_xpath).send_keys(adress)
    def enter_city(self):
        self.driver.find_element_by_xpath(self.city_xpath).send_keys("Toronto")
    def select_province(self):
        self.driver.find_element_by_xpath(self.province_xpath).click()
        self.driver.find_element_by_xpath(self.province_search_xpath).send_keys("Ontario")
        self.driver.find_element_by_xpath(self.ontario_xpath).click()
    def enter_postalcode(self,postal):
        self.driver.find_element_by_xpath(self.postalcode_xpath).send_keys(postal)
    def select_payment(self):
        self.driver.find_element_by_xpath(self.cash_on_delivery_xpath).click()
    def place_order(self):
        self.driver.find_element_by_xpath(self.place_order_xpath).click()




