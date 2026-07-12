from selenium.webdriver.common.by import By

##PAGE INPUT PERSONAL DETAILS
##PERSONAL DETAILS
FLD_FIRSTNAME               = (By.XPATH, "//input[@name='firstName']")
FLD_MIDNAME                 = (By.XPATH, "//input[@name='middleName']")
FLD_LASTNAME                = (By.XPATH, "//input[@name='lastName']")
FLD_EMPLOYEE_ID             = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Employee Id']]//input")
FLD_OTHER_ID                = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Other Id']]//input")
FLD_DRIVER_LICENSE_NUMBER   = (By.XPATH, "//label[contains(text(), 'License Number')]/following::input[1]")
FLD_LICENSE_EXP_DATE        = (By.XPATH, "//label[contains(text(), 'License Expiry Date')]/following::input[1]")
FLD_SSN_NUMBER              = (By.XPATH, "//label[contains(text(), 'SSN Number')]/following::input[1]")
DDL_NATIONALITY             = (By.XPATH, "//label[text()='Nationality']/following::div[@class='oxd-select-text-input'][1]")
DDL_MARITAL_STATUS          = (By.XPATH, "//label[text()='Marital Status']/following::div[@class='oxd-select-text-input'][1]")
FLD_DATE_OF_BIRTH           = (By.XPATH, "//label[contains(text(), 'Date of Birth')]/following::input[1]")
RDO_GENDER                  = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Gender']]//label[contains(normalize-space(), '{}')]")
BTN_SAVE_PERSONAL_DETAILS   = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]")

##CUSTOM FIELDS
DDL_BLOOD_TYPE              = (By.XPATH, "//label[text()='Blood Type']/following::div[@class='oxd-select-text-input'][1]")
FLD_TEST_FIELD              = (By.XPATH, "//label[contains(text(), 'Test_Field')]/following::input[1]")
BTN_SAVE_CUSTOM_FIELDS      = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[2]")
##END PAGE INPUT PERSONAL DETAILS

LBL_CONTACT_DETAILS                 = (By.XPATH, "(//a[normalize-space()='Contact Details'])[1]")
##PAGE CONTACT DETAILS
FLD_STREET1                 = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Street 1']]//input")
FLD_STREET2                 = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Street 2']]//input")
FLD_CITY                    = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='City']]//input")
FLD_STATE_PROVINCE          = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='State/Province']]//input")
FLD_ZIP_POSTALCODE          = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Zip/Postal Code']]//input")
DDL_COUNTRY                 = (By.XPATH, "//label[text()='Country']/following::div[@class='oxd-select-text-input'][1]")
FLD_TELP_HOME               = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Home']]//input")
FLD_TELP_MOBILE             = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Mobile']]//input")
FLD_TELP_WORK               = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Work']]//input")
FLD_WORK_EMAIL              = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Work Email']]//input")
FLD_OTHER_EMAIL             = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Other Email']]//input")
#pakai BTN_SAVE_GLOBAL
##END PAGE CONTACT DETAILS

LBL_EMERGENCY_CONTACT               = (By.XPATH, "(//a[normalize-space()='Emergency Contacts'])[1]")
##PAGE EMERGENCY CONTACTS
BTN_ADD_ASSIGNED_EMERGENCY_CONTACT  = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]")
FLD_NAME_EMERGENCYCONTACT           = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Name']]//input")
FLD_RELATIONSHIP_EMERGENCYCONTACT   = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Relationship']]//input")
FLD_TELP_HOME_EMERGENCYCONTACT      = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Home Telephone']]//input")
FLD_TELP_MOBILE_EMERGENCYCONTACT    = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Mobile']]//input")
FLD_TELP_WORK_EMERGENCYCONTACT      = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Work Telephone']]//input")
#pakai BTN_SAVE_GLOBAL
##END PAGE CONTACT DETAILS

LBL_DEPENDENTS                      = (By.XPATH, "(//a[normalize-space()='Dependents'])[1]")
##PAGE DEPENDENTS
BTN_ADD_ASSIGNED_DEPENDENTS         = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]")
FLD_NAME_DEPENDENTS                 = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Name']]//input")
DDL_RELATIONSHIP_DEPENDENTS         = (By.XPATH, "//label[text()='Relationship']/following::div[@class='oxd-select-text-input'][1]")
FLD_PLEASE_SPECIFY_DEPENDENTS       = (By.XPATH, "//label[contains(text(), 'Please Specify')]/following::input[1]")
FLD_DATE_OF_BIRTH_DEPENDENTS        = (By.XPATH, "//label[contains(text(), 'Date of Birth')]/following::input[1]")
#pakai BTN_SAVE_GLOBAL
##END PAGE DEPENDENTS

LBL_IMMIGRATION                     = (By.XPATH, "(//a[normalize-space()='Immigration'])[1]")
##PAGE IMMIGRATION
BTN_ADD_IMMIGRATION                 = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]")
RDO_DOCUMENT                        = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Document']]//label[contains(normalize-space(), '{}')]")
FLD_NUMBER                          = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Number']]//input")
FLD_ISSUED_DATE                     = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Issued Date']]//input")
FLD_EXPIRY_DATE                     = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Expiry Date']]//input")
FLD_ELIGIBLE_STATUS                 = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Eligible Status']]//input")
DDL_ISSUED_BY                       = (By.XPATH, "//label[text()='Issued By']/following::div[@class='oxd-select-text-input'][1]")
FLD_ELIGIBLE_REVIEW_DATE            = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Eligible Review Date']]//input")
FLD_COMMENTS                        = (By.XPATH, "(//textarea[@placeholder='Type Comments here'])[1]")
#pakai BTN_SAVE_GLOBAL
##ENDPAGE IMMIGRATION

LBL_QUALIFICATIONS                  = (By.XPATH, "(//a[normalize-space()='Qualifications'])[1]")
##PAGE QUALIFICATIONS
BTN_ADD_WORKEXPERIENCE              = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]")
FLD_COMPANY                         = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Company']]//input")
FLD_JOB_TITLE                       = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Job Title']]//input")
FLD_FROM                            = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='From']]//input")
FLD_TO                              = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='To']]//input")
FLD_COMMENTS_ADDWORKEXPERIENCE      = (By.XPATH, "(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[1]")
#pakai BTN_SAVE_GLOBAL

BTN_ADD_EDUCATION                   = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[2]")
DDL_LEVEL                           = (By.XPATH, "//label[text()='Level']/following::div[@class='oxd-select-text-input'][1]")
FLD_INSTITUTE                       = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Institute']]//input")
FLD_MAJOR_SPECIALIZATION            = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Major/Specialization']]//input")
FLD_YEAR                            = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Year']]//input")
FLD_GPA_SCORE                       = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='GPA/Score']]//input")
FLD_STARTDATE                       = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Start Date']]//input")
FLD_ENDDATE                         = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='End Date']]//input")
#pakai BTN_SAVE_GLOBAL

BTN_ADD_SKILL                       = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[3]")
FLD_SKILL                           = (By.XPATH, "//label[text()='Skill']/following::div[@class='oxd-select-text-input'][1]")
FLD_YEARS_OF_EXPERIENCE             = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Years of Experience']]//input")
FLD_COMMENTS_ADD_SKILL              = (By.XPATH, "(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[1]")
#pakai BTN_SAVE_GLOBAL

BTN_ADD_LANGUAGES                   = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[4]")
DDL_LANGUAGE                        = (By.XPATH, "//label[text()='Language']/following::div[@class='oxd-select-text-input'][1]")
DDL_FLUENCY                         = (By.XPATH, "//label[text()='Fluency']/following::div[@class='oxd-select-text-input'][1]")
DDL_COMPETENCY                      = (By.XPATH, "//label[text()='Competency']/following::div[@class='oxd-select-text-input'][1]")
FLD_COMMENTS_ADD_LANGUAGES          = (By.XPATH, "(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[1]")
#pakai BTN_SAVE_GLOBAL

BTN_ADD_LICENSE                     = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[5]")
DDL_LICENSE_TYPE                    = (By.XPATH, "//label[text()='License Type']/following::div[@class='oxd-select-text-input'][1]")
FLD_LICENSE_NUMBER                  = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='License Number']]//input")
FLD_ISSUEDDATE_ADD_LICENSE          = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Issued Date']]//input")
FLD_EXPIRYDATE_ADD_LICENSE          = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Expiry Date']]//input")
#pakai BTN_SAVE_GLOBAL

LBL_MEMBERSHIPS                     = (By.XPATH, "(//a[normalize-space()='Memberships'])[1]")
##
BTN_ADD_MEMBERSHIP                  = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]")
DDL_MEMBERSHIP                      = (By.XPATH, "//label[text()='Membership']/following::div[@class='oxd-select-text-input'][1]")
DDL_SUBSCRIPTION_PAID_BY            = (By.XPATH, "//label[text()='Subscription Paid By']/following::div[@class='oxd-select-text-input'][1]")
FLD_SUBSCRIPTION_AMT                = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Subscription Amount']]//input")
DDL_CURRENCY                        = (By.XPATH, "//label[text()='Currency']/following::div[@class='oxd-select-text-input'][1]")
FLD_SUBSCRIPTION_COMMENCE_DATE      = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Subscription Commence Date']]//input")
FLD_SUBSCRIPTION_RENEWAL_DATE       = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='Subscription Renewal Date']]//input")
#pakai BTN_SAVE_GLOBAL