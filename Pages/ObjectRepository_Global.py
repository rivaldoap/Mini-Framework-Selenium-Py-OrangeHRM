from selenium.webdriver.common.by import By


FLD_USERNAME                    = (By.XPATH, "//input[@placeholder='Username']")
FLD_PASSWORD                    = (By.XPATH, "//input[@placeholder='Password']")
BTN_LOGIN                       = (By.XPATH, "//button[normalize-space()='Login']")

LBL_PAGE_LOGIN                  = (By.XPATH, "//div[@class='orangehrm-login-slot']")
LBL_HEADER_DASHBOARD            = (By.XPATH, "//div[@class='oxd-topbar-header-title']")

LBL_TOAST           = (By.XPATH, "//*[@id='oxd-toaster_1']")
