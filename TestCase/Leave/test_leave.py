import os
import sys
import time

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
)

import pytest
from Utils.base_function import login
from Pages.ObjectRepository_Global import *
from Excel.Leave.excel_reader_leave_positive import (
    leave_positive as read_excel_positive
    )
from Utils.helper import *
from TestCase.Leave.ObjectRepository_Leave import *

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXCEL_ADMIN = os.path.join(BASE_DIR, "Excel", "Leave", "Leave - Positive.xlsx")

cek_pilihan_excel = read_excel_positive()

@pytest.mark.parametrize("data_excel", cek_pilihan_excel)
def test_leave(driver, data_excel):
    login(driver)
    navigate_to_menu(driver, EXCEL_ADMIN)

    input_text(driver, FLD_FROM_DATE, data_excel["FROM_DATE"])
    input_text(driver, FLD_TO_DATE, data_excel["TO_DATE"])
    click(driver, BTN_CLEAR_SHOW_LEAVE)
    click_dropdownlist_dynamic_label(driver, "Show Leave with Status", data_excel["SHOW_LEAVE_WITH_STATUS"])
    click_dropdownlist_dynamic_label(driver, "Leave Type", data_excel["LEAVE_TYPE"])

    input_text(driver, FLD_EMPLOYEE_NAME, data_excel["EMPLOYEE_NAME"])
    employee_name          = data_excel["EMPLOYEE_NAME"]
    if employee_name:
        locator_dinamis = (CLICK_FLD_EMPLOYEE_NAME[0], CLICK_FLD_EMPLOYEE_NAME[1].format(employee_name))
        click(driver, locator_dinamis)
    # if data_excel.get("SUB_UNIT"):
    click_dropdownlist_dynamic_label(driver, "Sub Unit", data_excel["SUB_UNIT"])

    if data_excel.get("INCLUDE_PAST_EMPLOYEES") and str(data_excel["INCLUDE_PAST_EMPLOYEES"]).strip().upper() == "Y":
        print("   [Radio Button] Excel = Y. Mengeklik Include Past Employees.")
        click(driver, RDO_INC_PAST_EMPLOYEES)
        
    elif data_excel.get("INCLUDE_PAST_EMPLOYEES") and str(data_excel["INCLUDE_PAST_EMPLOYEES"]).strip().upper() == "N":
        print("   [Radio Button] Excel = N. Dilewati sesuai request.")
        # dikosongkan karena (tidak ada fungsi click)
    
@pytest.mark.parametrize("data_excel", cek_pilihan_excel)
def test_apply_leave(driver, data_excel):
    login(driver)
    navigate_to_menu(driver, EXCEL_ADMIN)

    click_dropdownlist_dynamic_label(driver, "Leave Type", data_excel["LEAVE_TYPE"])
    input_text(driver, FLD_FROM_DATE, data_excel["FROM_DATE"])
    input_text(driver, FLD_TO_DATE, data_excel["TO_DATE"])
    click(driver, BTN_APPLY_LEAVE)

    assert_text_equals_validasi(driver, LBL_TOAST, data_excel["ASSERTION"])

    # if LBL_TOAST.is_displayed():
    #     assert_text_equals_validasi(driver, LBL_TOAST, data_excel["ASSERTION"])
    # else:
    #     assert_element_displayed(driver, LBL_TOAST)

