
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os, time
from sysmonlib import BugReportGenerator as bug
from sysmonlib import UIAutoBaseClass as UITest
os.chdir(os.path.dirname(os.path.abspath(__file__)))

url = "https://gene-drive.bmgf.io/"   
print("Starting GeneDrive test...", url)
try:
    # find the button with id = close-greeting-modal and click it
    driver = UITest.ChromeTest().open_url(url) 
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "close-greeting-modal").click()
    driver.implicitly_wait(2)       
    driver.find_element(By.ID, "run-elim-prob-matrices").click()
    
    # verify if matrix was displayed:
    driver.find_element(By.ID, "elim-prob-matrices")
    print("Validated presence of element with locator: ", "elim-prob-matrices")
    time.sleep(3)
    print("PASS:  GeneDrive test completed successfully.")
   
except Exception as e:
    print(e)
    print("Exception occurred. Generating bug report...")
    bug.generate_bug_report(e, url, title="Failure in GeneDriveSite")    

finally:
    try:
        driver.save_screenshot("screenshot.png")
    except Exception as screenshot_error:
        print("Failed to capture screenshot:", screenshot_error)
        
    if driver is not None:
        driver.quit()