from selenium.webdriver.common.by import By

FLD_FROM_DATE               = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='From Date']]//input")
FLD_TO_DATE                 = (By.XPATH, "//div[contains(@class, 'oxd-input-group')][.//label[text()='To Date']]//input")
BTN_CLEAR_SHOW_LEAVE        = (By.XPATH, "(//i[@class='oxd-icon bi-x --clear'])[1]") #secara default sudah terpilih Pending Approval
DDL_SHOW_LEAVE_WITH_STATUS  = (By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
DDL_LEAVE_TYPE              = (By.XPATH, "(//div)[56]")
FLD_EMPLOYEE_NAME           = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
CLICK_FLD_EMPLOYEE_NAME     = (By.XPATH, "//div[@role='listbox']//div[@role='option' and contains(normalize-space(), '{}')]")
DDL_SUB_UNIT                = (By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[3]")
RDO_INC_PAST_EMPLOYEES      = (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
BTN_SEARCH                  = (By.XPATH, "(//button[normalize-space()='Search'])[1]")

LBL_APPLY_LEAVE             = (By.XPATH, "//a[normalize-space()='Apply']")
BTN_APPLY_LEAVE             = (By.XPATH, "//button[normalize-space()='Apply']")