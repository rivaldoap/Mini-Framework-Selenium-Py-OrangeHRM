import os
import sys
import time

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
)

import pytest
from Utils.base_function import *
from Pages.ObjectRepository_Global import *
from Excel.PIM.excel_reader_pim_positive import (
    pim_positive as read_excel_positive
    )
from Utils.helper import *
from TestCase.PIM.ObjectRepository_PIM import *

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXCEL_PIM = os.path.join(BASE_DIR, "Excel", "PIM", "PIM - Positive.xlsx")

cek_pilihan_excel = read_excel_positive()

@pytest.mark.parametrize("data_excel", cek_pilihan_excel)
def test_pim(driver, data_excel):
    login(driver)
    navigate_to_menu(driver, EXCEL_PIM)

    functionInputText(driver, FLD_FIRSTNAME, data_excel["FIRST_NAME"])
    functionInputText(driver, FLD_MIDDLENAME, data_excel["MID_NAME"])
    functionInputText(driver, FLD_LASTNAME, data_excel["LAST_NAME"])
    functionInputText(driver, FLD_EMPLOYEEID, data_excel["EMPLOYEE_ID"])

    if data_excel["CREATE_LOGIN_DETAILS"] == "Y":
        functionClick(driver, RDO_CREATELOGINDETAILS)
        functionScrollByPixel(driver)

        functionInputText(driver, FLD_USERNAME, data_excel["USERNAME"])

        if data_excel["STATUS"] == "1":
            functionClick(driver, RDO_STATUS_ENABLE)
        elif data_excel["STATUS"] == "2":
            functionClick(driver, RDO_STATUS_DISABLE)
        
        functionInputText(driver, FLD_PASSWORD, data_excel["PASSWORD"])
        functionInputText(driver, FLD_CONFIRMPASSWORD, data_excel["CONFIRM_PASSWORD"])
        functionClick(driver, BTN_SAVE)

        # if data_excel["ASSERTION"] == "Successfully Saved":
        if data_excel["ASSERTION"] == "Successfully Saved" and assertTextEqualsValidasi(driver, LBL_TOAST, data_excel["ASSERTION"]):
            print("\nSuccessfully Saved")
        else:
            assertGetText(driver, TXT_ERRMSG_EMPID_EXIST)
            print("\nEmployee Id already exists")

        logout(driver)

    ###JIKA data_excel["CREATE_LOGIN_DETAILS"] != "Y" akan masuk kondisi ini
    else:
        functionClick(driver, BTN_SAVE)

        # if data_excel["ASSERTION"] == "Successfully Saved":
        #     if assertTextEqualsValidasi(driver, LBL_TOAST, data_excel["ASSERTION"]):
        #         print("\nSuccessfully Saved")

        if data_excel["ASSERTION"] == "Successfully Saved" and assertTextEqualsValidasi(driver, LBL_TOAST, data_excel["ASSERTION"]):
            print("\nSuccessfully Saved")
        else:
            assertGetText(driver, TXT_ERRMSG_EMPID_EXIST)
            print("\nEmployee Id already exists")

        logout(driver)
