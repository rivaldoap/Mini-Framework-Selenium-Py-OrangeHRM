import os
import sys
import time

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
)

import pytest
from Utils.base_function import login, logout
from Pages.ObjectRepository_Global import *
from Excel.Admin.excel_reader_admin_positive import (
    admin_positive as read_excel_positive)
from Utils.helper import *
from TestCase.Admin.ObjectRepository_Admin import *

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXCEL_ADMIN = os.path.join(BASE_DIR, "Excel", "Admin", "Admin - Positive.xlsx")

cek_pilihan_excel = read_excel_positive()

@pytest.mark.parametrize("data_excel", cek_pilihan_excel)
def test_admin_navigation(driver, data_excel):
    login(driver)
    navigate_to_menu(driver, EXCEL_ADMIN)

    functionClick(driver, BTN_ADD)

    employee_name          = data_excel["EMPLOYEE_NAME"]

    functionClickDDL_WithLabel(driver, "User Role", data_excel["USER_ROLE"])
    functionInputText(driver, FLD_EMPLOYEENAME, data_excel["EMPLOYEE_NAME"])
    time.sleep(1.5)
    if employee_name:
        locator_dinamis = (CLICK_FLD_EMPLOYEENAME[0], CLICK_FLD_EMPLOYEENAME[1].format(employee_name))
        functionClick(driver, locator_dinamis)

    functionClickDDL_WithLabel(driver, "Status", data_excel["STATUS"])
    functionInputText(driver, FLD_USERNAME, data_excel["USERNAME"])
    functionInputText(driver, FLD_PASSWORD, data_excel["PASSWORD"])
    functionInputText(driver, FLD_CONFIRMPASSWORD, data_excel["CONFIRM_PASSWORD"])
    functionScrollToElement(driver, BTN_SAVE)
    functionClick(driver, BTN_SAVE)
    assertTextEqualsValidasi(driver, LBL_TOAST, data_excel["ASSERTION"])

    logout(driver)