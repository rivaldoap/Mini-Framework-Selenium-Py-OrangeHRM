import os
import sys
import time

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
)

import pytest
from Utils.base_function import *
from Pages.ObjectRepository_Global import *
from Excel.MyInfo.excel_reader_myinfo_positive import (
    my_info_positive as read_excel_positive
    )
from Utils.helper import *
from TestCase.MyInfo.ObjectRepository_MyInfo import *
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXCEL_MY_INFO = os.path.join(BASE_DIR, "Excel", "MyInfo", "My Info - Positive.xlsx")

cek_pilihan_excel = read_excel_positive()

@pytest.mark.parametrize("data_excel", cek_pilihan_excel)
def test_my_info(driver, data_excel):
    login(driver)
    navigate_to_menu(driver, EXCEL_MY_INFO)

    functionInputText(driver, FLD_FIRSTNAME, data_excel["FIRST_NAME"])
    functionInputText(driver, FLD_MIDNAME, data_excel["MID_NAME"])
    functionInputText(driver, FLD_LASTNAME, data_excel["LAST_NAME"])
    functionInputText(driver, FLD_EMPLOYEE_ID, data_excel["EMPLOYEE_ID"])
    functionInputText(driver, FLD_OTHER_ID, data_excel["OTHER_ID"])
    functionInputText(driver, FLD_DRIVER_LICENSE_NUMBER, data_excel["DRIVER_LICENSE_NUMBER"])
    functionInputText(driver, FLD_LICENSE_EXP_DATE, data_excel["LICENSE_EXP_DATE"])
    
    if Exist(driver, FLD_SSN_NUMBER):
        functionInputText(driver, FLD_SSN_NUMBER, data_excel["SSN_NUMBER"])

    """=========================NATIONALITY========================="""
    Nationality = functionGetTextDDL_ByLabel(driver, "Nationality")
    if Nationality == data_excel["NATIONALITY"]:
        print(f"Nationality '{Nationality}'. Skip")
        pass
    else:
        print(f"Nationality di web '{Nationality}' berbeda dengan excel. Melakukan Input")
        functionSelectDDL_ByLabel(driver, "Nationality", data_excel["NATIONALITY"])

    """=========================MARITAL STATUS========================="""
    status_MaritalStatus = functionGetTextDDL_ByLabel(driver, "Marital Status")
    if status_MaritalStatus == data_excel["MARITAL_STATUS"]:
        print(f"Status '{status_MaritalStatus}'. Skip")
        pass
    else:
        print(f"Status di web '{status_MaritalStatus}' berbeda dengan excel. Melakukan Input")
        functionSelectDDL_ByLabel(driver, "Marital Status", data_excel["MARITAL_STATUS"])

    functionInputText(driver, FLD_DATE_OF_BIRTH, data_excel["DATE_OF_BIRTH"])
    functionSelectRDO(driver, RDO_GENDER, data_excel["GENDER"])
    functionClick(driver, BTN_SAVE_PERSONAL_DETAILS)
    assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Updated")

    """=========================BLOOD TYPE========================="""
    Blood_Type = functionGetTextDDL_ByLabel(driver, "Blood Type")
    if Blood_Type == data_excel["BLOOD_TYPE"]:
        print(f"Status '{Blood_Type}'. Skip")
        pass
    else:
        print(f"Blood Type di web '{Blood_Type}' berbeda dengan excel. Melakukan Input")
        functionSelectDDL_ByLabel(driver, "Blood Type", data_excel["BLOOD_TYPE"])
    
    functionInputText(driver, FLD_TEST_FIELD, data_excel["TEST_FIELD"])
    functionClick(driver, BTN_SAVE_CUSTOM_FIELDS)
    assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Saved")

    functionClick(driver, LBL_CONTACT_DETAILS)
    functionInputText(driver, FLD_STREET1, data_excel["STREET1"])
    functionInputText(driver, FLD_STREET2, data_excel["STREET2"])
    functionInputText(driver, FLD_CITY, data_excel["CITY"])
    functionInputText(driver, FLD_STATE_PROVINCE, data_excel["STATE_PROVINCE"])
    functionInputText(driver, FLD_ZIP_POSTALCODE, data_excel["ZIP_POSTALCODE"])
    
    """=========================COUNTRY========================="""
    Country = functionGetTextDDL_ByLabel(driver, "Country")
    if Country == data_excel["COUNTRY"]:
        print(f"Country '{Country}'. Skip")
        pass
    else:
        print(f"Country di web '{Country}' berbeda dengan excel. Melakukan Input")
        functionSelectDDL_ByLabel(driver, "Country", data_excel["COUNTRY"])

    functionInputText(driver, FLD_TELP_HOME, data_excel["TELP_HOME"])
    functionInputText(driver, FLD_TELP_MOBILE, data_excel["TELP_MOBILE"])
    functionInputText(driver, FLD_TELP_WORK, data_excel["TELP_WORK"])
    functionInputText(driver, FLD_WORK_EMAIL, data_excel["WORK_EMAIL"])
    functionInputText(driver, FLD_OTHER_EMAIL, data_excel["OTHER_EMAIL"])
    functionClick(driver, BTN_SAVE_GLOBAL)
    assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Updated")

    functionClick(driver, LBL_EMERGENCY_CONTACT)
    functionClick(driver, BTN_ADD_ASSIGNED_EMERGENCY_CONTACT)
    functionInputText(driver, FLD_NAME_EMERGENCYCONTACT, data_excel["NAME_EMERGENCYCONTACT"])
    functionInputText(driver, FLD_RELATIONSHIP_EMERGENCYCONTACT, data_excel["RELATIONSHIP_EMERGENCYCONTACT"])
    functionInputText(driver, FLD_TELP_HOME_EMERGENCYCONTACT, data_excel["TELP_HOME_EMERGENCYCONTACT"])
    functionInputText(driver, FLD_TELP_MOBILE_EMERGENCYCONTACT, data_excel["MOBILE_EMERGENCYCONTACT"])
    functionInputText(driver, FLD_TELP_WORK_EMERGENCYCONTACT, data_excel["TELP_WORK_EMERGENCYCONTACT"])
    functionClick(driver, BTN_SAVE_GLOBAL)
    assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Saved")

    functionClick(driver, LBL_DEPENDENTS)
    functionClick(driver, BTN_ADD_ASSIGNED_DEPENDENTS)
    functionInputText(driver, FLD_NAME_DEPENDENTS, data_excel["NAME_DEPENT"])

    functionSelectDDL_ByLabel(driver, "Relationship", data_excel["RELATIONSHIP_DEPENT"])

    if data_excel["RELATIONSHIP_DEPENT"] == "Other":
        functionInputText(driver, FLD_PLEASE_SPECIFY_DEPENDENTS, data_excel["PLEASE_SPECIFY_DEPENT"])

    functionInputText(driver, FLD_DATE_OF_BIRTH_DEPENDENTS, data_excel["DATEOFBIRTH_DEPENT"])
    functionClick(driver, BTN_SAVE_GLOBAL)
    assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Saved")

    functionClick(driver, LBL_IMMIGRATION)
    functionClick(driver, BTN_ADD_IMMIGRATION)
    time.sleep(2)
    functionSelectRDO(driver, RDO_DOCUMENT, data_excel["DOC_PASSPORT_OR_VISA"])
    functionInputText_ByLabel(driver, "Number", data_excel["NUMBER"])
    functionInputText_ByLabel(driver, "Issued Date", data_excel["ISSUED_DATE"])
    functionInputText_ByLabel(driver, "Expiry Date", data_excel["EXP_DATE"])
    functionInputText_ByLabel(driver, "Eligible Status", data_excel["ELIGIBLE_STATUS"])
    
    """=========================ISSUED BY========================="""
    Issued_By = functionGetTextDDL_ByLabel(driver, "Issued By")
    if Issued_By == data_excel["ISSUED_BY"]:
        print(f"Issued By '{Issued_By}'. Skip")
        pass
    else:
        print(f"Issued_By di web '{Issued_By}' berbeda dengan excel. Melakukan Input")
        functionSelectDDL_ByLabel(driver, "Issued By", data_excel["ISSUED_BY"])

    functionInputText_ByLabel(driver, "Eligible Review Date", data_excel["ELIGIBLE_REVIEW_DATE"])
    functionInputText_ByLabel(driver, "Comments", data_excel["COMMENTS"])
    functionClick(driver, BTN_SAVE_GLOBAL)
    assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Saved")
    
    functionClick(driver, LBL_QUALIFICATIONS)
    if data_excel["DECISION_WORKEXPERIENCE_Y_N"] == "Y":
        functionClick(driver, BTN_ADD_WORKEXPERIENCE)
        functionInputText(driver, FLD_COMPANY, data_excel["WORKEXPRERIENCE_COMPANY"])
        functionInputText(driver, FLD_JOB_TITLE, data_excel["WORKEXPRERIENCE_JOB_TITLE"])
        functionInputText(driver, FLD_FROM, data_excel["WORKEXPERIENCE_FROM"])
        functionInputText(driver, FLD_TO, data_excel["WORKEXPERIENCE_TO"])
        functionInputText_ByLabel(driver, "Comment", data_excel["WORKEXPERIENCE_COMMENT"])
        functionClick(driver, BTN_SAVE_GLOBAL)

        assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Saved")

    elif data_excel["DECISION_WORKEXPERIENCE_Y_N"] == "N":
        pass
    else:
        print("\nDATA EXCEL KOSONG atau TIDAK VALID, ONLY : (Y & N)")
    
    if data_excel["DECISION_EDUCATION_Y_N"] == "Y":
        functionClick(driver, BTN_ADD_EDUCATION)

        """=========================LEVEL========================="""
        Level = functionGetTextDDL_ByLabel(driver, "Level")
        if Level == data_excel["EDUCATION_LEVEL"]:
            print(f"Issued By '{Level}'. Skip")
            pass
        else:
            print(f"Level di web '{Level}' berbeda dengan excel. Melakukan Input")
            functionSelectDDL_ByLabel(driver, "Level", data_excel["EDUCATION_LEVEL"])

        functionInputText(driver, FLD_INSTITUTE, data_excel["EDUCATION_INSTITUTE"])
        functionInputText(driver, FLD_MAJOR_SPECIALIZATION, data_excel["EDUCATION_MAJOR_SPECIALIZATION"])
        functionInputText(driver, FLD_YEAR, data_excel["EDUCATION_YEAR"])
        functionInputText(driver, FLD_GPA_SCORE, data_excel["EDUCATION_GPA_SCORE"])
        functionInputText(driver, FLD_STARTDATE, data_excel["EDUCATION_START_DATE"])
        functionInputText(driver, FLD_ENDDATE, data_excel["EDUCATION_END_DATE"])
        functionClick(driver, BTN_SAVE_GLOBAL)
        
        assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Saved")
    
    elif data_excel["DECISION_EDUCATION_Y_N"] == "N":
        pass
    else:
        print("\nDATA EXCEL KOSONG atau TIDAK VALID, ONLY : (Y & N)")

    if data_excel["DECISION_ADDSKILL_Y_N"] == "Y":
        functionClick(driver, BTN_ADD_SKILL)

        """=========================SKILL========================="""
        Skill = functionGetTextDDL_ByLabel(driver, "Skill")
        if Skill == data_excel["ADDSKILL_SKILL"]:
            print(f"Skill '{Skill}'. Skip")
            pass
        else:
            print(f"Skill di web '{Skill}' berbeda dengan excel. Melakukan Input")
            functionSelectDDL_ByLabel(driver, "Skill", data_excel["ADDSKILL_SKILL"])

        functionInputText(driver, FLD_YEARS_OF_EXPERIENCE, data_excel["ADDSKILL_YEARS_OF_EXPERIENCE"])
        functionInputText(driver, FLD_COMMENTS_ADD_SKILL, data_excel["ADDSKILL_COMMENTS"])
        functionClick(driver, BTN_SAVE_GLOBAL)

        assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Saved")

    elif data_excel["DECISION_ADDSKILL_Y_N"] == "Y":
        pass
    else:
        print("\nDATA EXCEL KOSONG atau TIDAK VALID, ONLY : (Y & N)")

    if data_excel["DECISION_ADDLANGUAGES_Y_N"] == "Y":
        functionClick(driver, BTN_ADD_LANGUAGES)
        time.sleep(2)

        """=========================LANGUAGE========================="""
        Language = functionGetTextDDL_ByLabel(driver, "Language")
        if Language == data_excel["ADDLANGUAGE_LANGUAGE"]:
            print(f"Language '{Language}'. Skip")
            pass
        else:
            print(f"Language di web '{Language}' berbeda dengan excel. Melakukan Input")
            functionSelectDDL_ByLabel(driver, "Language", data_excel["ADDLANGUAGE_LANGUAGE"])

        """=========================FLUENCY========================="""
        Fluency = functionGetTextDDL_ByLabel(driver, "Fluency")
        if Fluency == data_excel["ADDLANGUAGE_FLUENCY"]:
            print(f"Fluency '{Fluency}'. Skip")
            pass
        else:
            print(f"Fluency di web '{Fluency}' berbeda dengan excel. Melakukan Input")
            functionSelectDDL_ByLabel(driver, "Fluency", data_excel["ADDLANGUAGE_FLUENCY"])

        """=========================COMPETENCY========================="""
        Competency = functionGetTextDDL_ByLabel(driver, "Competency")
        if Competency == data_excel["ADDLANGUAGE_COMPETENCY"]:
            print(f"Competency '{Competency}'. Skip")
            pass
        else:
            print(f"Competency di web '{Competency}' berbeda dengan excel. Melakukan Input")
            functionSelectDDL_ByLabel(driver, "Competency", data_excel["ADDLANGUAGE_COMPETENCY"])

        functionInputText(driver, FLD_COMMENTS_ADD_SKILL, data_excel["ADDLANGUAGE_COMMENTS"])
        functionClick(driver, BTN_SAVE_GLOBAL)

        assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Saved")
    
    elif data_excel["DECISION_ADDLANGUAGES_Y_N"] == "N":
        pass
    else:
        print("\nDATA EXCEL KOSONG atau TIDAK VALID, ONLY : (Y & N)")

    if data_excel["DECISION_ADDLICENSE_Y_N"] == "Y":
        functionClick(driver, BTN_ADD_LICENSE)

        """=========================LICENSE TYPE========================="""
        License_Type = functionGetTextDDL_ByLabel(driver, "License Type")
        if License_Type == data_excel["ADDLICENSE_LICENSETYPE"]:
            print(f"License Type '{License_Type}'. Skip")
            pass
        else:
            print(f"License Type di web '{License_Type}' berbeda dengan excel. Melakukan Input")
            functionSelectDDL_ByLabel(driver, "License Type", data_excel["ADDLICENSE_LICENSETYPE"])

        functionInputText(driver, FLD_LICENSE_NUMBER, data_excel["ADDLICENSE_LICENSENUMBER"])
        functionInputText(driver, FLD_ISSUEDDATE_ADD_LICENSE, data_excel["ADDLICENSE_ISSUEDDATE"])
        functionInputText(driver, FLD_EXPIRYDATE_ADD_LICENSE, data_excel["ADDLICENSE_EXPIRYDATE"])
        functionClick(driver, BTN_SAVE_GLOBAL)

        assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Saved")
    
    elif data_excel["DECISION_ADDLICENSE_Y_N"] == "N":
        pass
    else:
        print("\nDATA EXCEL KOSONG atau TIDAK VALID, ONLY : (Y & N)")

    functionClick(driver, LBL_MEMBERSHIPS)
    functionClick(driver, BTN_ADD_MEMBERSHIP)

    """=========================MEMBERSHIP========================="""
    Membership = functionGetTextDDL_ByLabel(driver, "Membership")
    if Membership == data_excel["MEMBERSHIP"]:
        print(f"Membership '{Membership}'. Skip")
        pass
    else:
        print(f"Membership di web '{Membership}' berbeda dengan excel. Melakukan Input")
        functionSelectDDL_ByLabel(driver, "Membership", data_excel["MEMBERSHIP"])

    """=========================SUBSCRIPTION PAID BY========================="""
    Subscription_Paid_By = functionGetTextDDL_ByLabel(driver, "Subscription Paid By")
    if Subscription_Paid_By == data_excel["SUBS_PAID_BY"]:
        print(f"Subscription Paid By '{Subscription_Paid_By}'. Skip")
        pass
    else:
        print(f"Subscription Paid By di web '{Subscription_Paid_By}' berbeda dengan excel. Melakukan Input")
        functionSelectDDL_ByLabel(driver, "Subscription Paid By", data_excel["SUBS_PAID_BY"])

    functionInputText(driver, FLD_SUBSCRIPTION_AMT, data_excel["SUBS_AMT"])

    """=========================CURRENCY========================="""
    Currency = functionGetTextDDL_ByLabel(driver, "Currency")
    if Currency == data_excel["SUBS_PAID_BY"]:
        print(f"Currency '{Currency}'. Skip")
        pass
    else:
        print(f"Currency di web '{Currency}' berbeda dengan excel. Melakukan Input")
        functionSelectDDL_ByLabel(driver, "Currency", data_excel["CURRENCY"])

    functionInputText_ByLabel(driver, "Subscription Commence Date", data_excel["SUBS_COMMENCEDATE"])
    functionInputText_ByLabel(driver, "Subscription Renewal Date", data_excel["SUBS_RENEWALDATE"])
    functionClick(driver, BTN_SAVE_GLOBAL)

    assertTextEqualsValidasi(driver, LBL_TOAST, "Successfully Saved")