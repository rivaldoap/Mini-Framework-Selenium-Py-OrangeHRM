from selenium.webdriver.common.by import By

FLD_EMPLOYEENAME                = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
CLICK_FLD_EMPLOYEENAME          = (By.XPATH, "//div[@role='listbox']//div[@role='option' and contains(normalize-space(), '{}')]")
DDL_EVENT                       = (By.XPATH, "(//div[contains(text(),'-- Select --')])[1]")
DDL_CURRENCY                    = (By.XPATH, "(//div[contains(text(),'-- Select --')])[2]")
FLD_REMARKS                     = (By.XPATH, "(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[1]")
BTN_CREATE                      = (By.XPATH, "//button[normalize-space()='Create']")
        
TXT_REFERENCE_ID                = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
TXT_REFERENCE_ID_ASSIGNCLAIM    = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")