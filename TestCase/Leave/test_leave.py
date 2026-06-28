import os
import sys
import time

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
)

import pytest
from Utils.base_function import *
from Pages.ObjectRepository_Global import *
from Excel.Leave.excel_reader_leave_positive import (
    leave_positive as read_excel_positive
    )
from Utils.helper import *
from TestCase.Leave.ObjectRepository_Leave import *

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXCEL_LEAVE = os.path.join(BASE_DIR, "Excel", "Leave", "Leave - Positive.xlsx")

cek_pilihan_excel = read_excel_positive()

@pytest.mark.parametrize("data_excel", cek_pilihan_excel)
def test_leave_list(driver, data_excel):
    login(driver)
    navigate_to_menu(driver, EXCEL_LEAVE)

    functionInputText(driver, FLD_FROM_DATE, data_excel["FROM_DATE"])
    functionInputText(driver, FLD_TO_DATE, data_excel["TO_DATE"])
    functionClick(driver, BTN_CLEAR_SHOW_LEAVE)
    functionClickDDL_WithLabel(driver, "Show Leave with Status", data_excel["SHOW_LEAVE_WITH_STATUS"])
    functionClickDDL_WithLabel(driver, "Leave Type", data_excel["LEAVE_TYPE"])

    functionInputText(driver, FLD_EMPLOYEE_NAME, data_excel["EMPLOYEE_NAME"])
    employee_name          = data_excel["EMPLOYEE_NAME"]
    if employee_name:
        locator_dinamis = (CLICK_FLD_EMPLOYEE_NAME[0], CLICK_FLD_EMPLOYEE_NAME[1].format(employee_name))
        functionClick(driver, locator_dinamis)
    # if data_excel.get("SUB_UNIT"):
    # functionClickDDL_WithLabel(driver, "Sub Unit", data_excel["SUB_UNIT"])

    if data_excel["INCLUDE_PAST_EMPLOYEES"] == "Y":
        functionClick(driver, RDO_INC_PAST_EMPLOYEES)
        print("   [Radio Button] Excel = Y. Mengeklik Include Past Employees.")
    else:
        print("   [Radio Button] Excel = N. Dilewati sesuai request.")
        # dikosongkan karena (tidak ada fungsi click)
    
    functionClick(driver, BTN_SEARCH)

    if data_excel["ASSERTION"] == "Successfully Saved" and assertTextEqualsValidasi(driver, LBL_TOAST, data_excel["ASSERTION"]):
        print("\nSuccessfully Saved")
    elif data_excel["ASSERTION"] == "No Records Found" and assertTextEqualsValidasi(driver, LBL_TOAST, data_excel["ASSERTION"]):
        print("\nNo Records Found")
    
    logout(driver)
    
@pytest.mark.parametrize("data_excel", cek_pilihan_excel)
def test_apply_leave(driver, data_excel):
    login(driver)
    navigate_to_menu(driver, EXCEL_LEAVE)

    functionClickDDL_WithLabel(driver, "Leave Type", data_excel["LEAVE_TYPE"])
    functionInputText(driver, FLD_FROM_DATE, data_excel["FROM_DATE"])
    functionInputText(driver, FLD_TO_DATE, data_excel["TO_DATE"])
    functionClick(driver, BTN_APPLY_LEAVE)

    assertTextEqualsValidasi(driver, LBL_TOAST, data_excel["ASSERTION"])

    # if LBL_TOAST.is_displayed():
    #     assertTextEqualsValidasi(driver, LBL_TOAST, data_excel["ASSERTION"])
    # else:
    #     assertElementDisplayed(driver, LBL_TOAST)

    logout(driver)
