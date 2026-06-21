from selenium.webdriver.common.by import By

BTN_ADD             = (By.XPATH, "//button[normalize-space()='Add']")
DDL_USERROLE        = (By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
FLD_EMPLOYEENAME    = (By.XPATH, "//input[@placeholder='Type for hints...']")
CLICK_FLD_EMPLOYEENAME  = (By.XPATH, "//div[@role='listbox']//div[@role='option' and contains(normalize-space(), '{}')]")
DDL_STATUS          = (By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
FLD_USERNAME        = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
FLD_PASSWORD        = (By.XPATH, "(//input[@type='password'])[1]")
FLD_CONFIRMPASSWORD = (By.XPATH, "(//input[@type='password'])[2]")
BTN_SAVE            = (By.XPATH, "//button[normalize-space()='Save']")
