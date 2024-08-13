import pytest
from faker import Faker
from pages.parabank_register_page import ParaBankRegisterPage
from utils.screenshot_extensions import ScreenShotExtensions
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_parabank_registration(initialize_driver):
    driver = initialize_driver
    para_bank_home_page = ParaBankRegisterPage(driver)
    # open the main page
    para_bank_home_page.open_page(os.getenv("URL_PARA_BANK"))
    ScreenShotExtensions.take_standard_screenshot(driver, "ParaBank_HomePage")
    # navigate to registration page by clicking on registration link
    para_bank_home_page.navigate_to_register_page()
    # Enter the data for Registration
    fake = Faker()
    para_bank_home_page.verify_registration_form_and_fill_details(fake.first_name(), fake.last_name(), fake.address(),
                                                                  fake.city(),
                                                                  fake.state(), fake.zipcode(),
                                                                  fake.phone_number(), fake.ssn()
                                                                  , "Derik", "Frost12@", "Frost12@")
    ScreenShotExtensions.take_standard_screenshot(driver, "ParaBank_Fill_Registartion_Form")
