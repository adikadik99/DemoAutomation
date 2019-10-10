from selenium.webdriver.support.ui import Select
class RegisterPage():

    def __init__(self,driver):
        self.driver = driver
        self.firstname_textbox_xpath = "//input[@placeholder='First Name']"
        self.lastname_textbox_xpath = "//input[@placeholder='Last Name']"
        self.adress_textbox_xpath = "//textarea[@class='form-control ng-pristine ng-untouched ng-valid']"
        self.email_textbox_xpath = "//input[@class='form-control ng-pristine ng-untouched ng-valid-email ng-invalid ng-invalid-required']"
        self.phone_textbox_xpath = "//input[@class='form-control ng-pristine ng-untouched ng-invalid ng-invalid-required ng-valid-pattern']"
        self.gender_male_xpath = "//label[1]//input[1]"
        self.gender_female_xpath ="//label[2]//input[1]"
        self.hobbies_cricket_chkbox_xpath ="//input[@id='checkbox1']"
        self.hobbies_movies_chkbox_xpath ="//input[@id='checkbox2']"
        self.hobbies_hockey_chkbox_xpath ="//input[@id='checkbox3']"
        self.language_drpdwn_xpath ="//div[@id='msdd']"
        self.skills_drpdwn_xpath ="//select[@id='Skills']"
        self.countries1_drpdwn_xpath ="//select[@id='countries']"
        self.countries2_drpdown_xpath ="//span[@class='select2-selection select2-selection--single']"
        self.countries2_search_xpath ="//input[@class='select2-search__field']"
        self.year_drpdwn_xpath ="//select[@id='yearbox']"
        self.month_drpdwn_xpath ="//select[@placeholder='Month']"
        self.day_drpdwn_xpath ="//select[@id='daybox']"
        self.password_textbox_xpath ="//input[@id='firstpassword']"
        self.password_confirm_textbox_xpath ="//input[@id='secondpassword']"
        self.submit_button_xpath="//button[@id='submitbtn']"
        self.empty_space_xpath= "//form[@id='basicBootstrapForm']"

    def enter_firstname(self, firstname):
        self.driver.find_element_by_xpath(self.firstname_textbox_xpath).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element_by_xpath(self.lastname_textbox_xpath).send_keys(lastname)

    def enter_adress(self,adress):
        self.driver.find_element_by_xpath(self.adress_textbox_xpath).send_keys(adress)

    def enter_email(self,email):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element_by_xpath(self.phone_textbox_xpath).send_keys(phone)

    def click_male(self):
        self.driver.find_element_by_xpath(self.gender_male_xpath).click()

    def click_female(self):
        self.driver.find_element_by_xpath(self.gender_female_xpath).click()

    def click_cricket(self):
        self.driver.find_element_by_xpath(self.hobbies_cricket_chkbox_xpath).click()

    def click_movies(self):
        self.driver.find_element_by_xpath(self.hobbies_movies_chkbox_xpath).click()

    def click_hockey(self):
        self.driver.find_element_by_xpath(self.hobbies_hockey_chkbox_xpath).click()

    def select_language(self):
        self.driver.find_element_by_xpath("//div[@id='msdd']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Arabic')]").click()
    def select_skills(self):
        element = self.driver.find_element_by_xpath(self.skills_drpdwn_xpath)
        drp = Select(element)
        drp.select_by_visible_text("AutoCAD")

    def select_countries1(self):
        element = self.driver.find_element_by_xpath(self.countries1_drpdwn_xpath)
        drp = Select(element)
        drp.select_by_visible_text("Canada")

    def select_countries2(self):
        self.driver.find_element_by_xpath(self.countries2_drpdown_xpath).click()
        self.driver.find_element_by_xpath(self.countries2_search_xpath).send_keys("J")
        self.driver.find_element_by_xpath("//li[@class='select2-results__option select2-results__option--highlighted']").click()

    def select_year(self):
        element = self.driver.find_element_by_xpath(self.year_drpdwn_xpath)
        drp = Select(element)
        drp.select_by_visible_text("1989")

    def select_month(self):
        element = self.driver.find_element_by_xpath(self.month_drpdwn_xpath)
        drp = Select(element)
        drp.select_by_visible_text("October")

    def select_day(self):
        element = self.driver.find_element_by_xpath(self.day_drpdwn_xpath)
        drp = Select(element)
        drp.select_by_visible_text("13")

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def confirm_password(self,password):
        self.driver.find_element_by_xpath(self.password_confirm_textbox_xpath).send_keys(password)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()



