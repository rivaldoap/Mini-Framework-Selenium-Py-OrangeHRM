import os
import sys
import time

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
)

import pytest
from Utils.base_function import *
from Pages.ObjectRepository_Global import *
from Excel.Claim.excel_reader_claim_positive import (
    claim_submitclaim_positive as read_excel_positive_submit_claim,
    claim_assign_positive as read_excel_positive_assign
    )
from Utils.helper import *
from TestCase.Claim.ObjectRepository_Claim import *

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXCEL_CLAIM = os.path.join(BASE_DIR, "Excel", "Claim", "Claim - Positive.xlsx")

cek_pilihan_excel = read_excel_positive_submit_claim() and read_excel_positive_assign()

@pytest.mark.parametrize("data_excel", cek_pilihan_excel)
def test_submit_claim(driver, data_excel):
    login(driver)
    navigate_to_menu(driver, EXCEL_CLAIM)

    if data_excel["SUBMENU"] == "Submit Claim":
        functionClickDDL_WithLabel(driver, "Event", data_excel["EVENT"])
        functionClickDDL_WithLabel(driver, "Currency", data_excel["CURRENCY"])
        functionInputText(driver, FLD_REMARKS, data_excel["REMARKS"])
    
        functionClick(driver, BTN_CREATE)
    
        assertTextEqualsValidasi(driver, LBL_TOAST, data_excel["ASSERTION"])
    
        reference_id = assertGetText(driver, TXT_REFERENCE_ID)
        print(f"\nReference ID : {reference_id}\n")

    elif data_excel["SUBMENU"] == "Assign Claim":
        employee_name          = data_excel["EMPLOYEE_NAME"]
        functionInputText(driver, FLD_EMPLOYEENAME, data_excel["EMPLOYEE_NAME"])
        time.sleep(1.5)
        if employee_name:
            locator_dinamis = (CLICK_FLD_EMPLOYEENAME[0], CLICK_FLD_EMPLOYEENAME[1].format(employee_name))
            functionClick(driver, locator_dinamis)
        
        functionClickDDL_WithLabel(driver, "Event", data_excel["EVENT"])
        functionClickDDL_WithLabel(driver, "Currency", data_excel["CURRENCY"])
        functionInputText(driver, FLD_REMARKS, data_excel["REMARKS"])
    
        functionClick(driver, BTN_CREATE)
    
        assertTextEqualsValidasi(driver, LBL_TOAST, data_excel["ASSERTION"])

        reference_id = assertGetText(driver, TXT_REFERENCE_ID_ASSIGNCLAIM)
        print(f"\nReference ID : {reference_id}\n")

        logout(driver)
        