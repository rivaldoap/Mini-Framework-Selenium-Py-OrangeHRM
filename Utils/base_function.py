import os
import sys


sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
)

from Utils.driver_factory import start_browser
from _Data.Login.excel_reader_login import get_login_data
from Utils.helper import *
from Pages.ObjectRepository_Global import *

def login(driver):
    # driver = start_browser()
    # GET DATA FROM EXCEL
    data = get_login_data()
    # OPEN URL
    driver.get(data["URL"])
    assertElementDisplayed(driver, LBL_PAGE_LOGIN)

    functionInputText(driver, FLD_USERNAME, data["USERNAME"])
    functionInputText(driver, FLD_PASSWORD, data["PASSWORD"])
    functionClick(driver, BTN_LOGIN)
    assertElementDisplayed(driver, LBL_HEADER_DASHBOARD)
