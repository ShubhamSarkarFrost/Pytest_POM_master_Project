from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class ParaBankRegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.RegisterPagelink = (By.XPATH, "//a[contains(@href,'register.htm')]")
        self.firstname = (By.ID, 'customer.firstName')
        self.lastname = (By.ID, 'customer.lastName')
        self.address = (By.ID, 'customer.address.street')
        self.city = (By.ID, 'customer.address.city')
        self.state = (By.ID, 'customer.address.state')
        self.zipcode = (By.ID, 'customer.address.zipCode')
        self.phoneno = (By.ID, 'customer.phoneNumber')
        self.ssn = (By.ID, 'customer.ssn')
        self.username = (By.ID, 'customer.username')
        self.password = (By.ID, 'customer.password')
        self.confirmpwd = (By.ID, 'repeatedPassword')
        self.confirmBtn = (By.XPATH, "//input[@value='Register']")

    def open_page(self, url):
        self.driver.get(url)


    def navigate_to_register_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(*self.RegisterPagelink))).click()
        except Exception:
            print("the Register link is not available")

    def verify_registration_form_and_fill_details(self, first_name, last_name, add_ress, ci_ty, sta_te, zip_code,
                                                  phone_no,
                                                  ss_n, user_name, pass_word, confirm_password):
        self.driver.find_element(*self.firstname).send_keys(first_name)
        self.driver.find_element(*self.lastname).send_keys(last_name)
        self.driver.find_element(*self.address).send_keys(add_ress)
        self.driver.find_element(*self.city).send_keys(ci_ty)
        self.driver.find_element(*self.state).send_keys(sta_te)
        self.driver.find_element(*self.zipcode).send_keys(zip_code)
        self.driver.find_element(*self.phoneno).send_keys(phone_no)
        self.driver.find_element(*self.ssn).send_keys(ss_n)
        self.driver.find_element(*self.username).send_keys(user_name)
        self.driver.find_element(*self.password).send_keys(pass_word)
        self.driver.find_element(*self.confirmpwd).send_keys(confirm_password)
        self.driver.find_element(*self.confirmBtn).click()
