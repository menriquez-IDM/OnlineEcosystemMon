
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path
import os, sys, time

os.chdir(str(Path(sys.argv[0]).parent))
sys.path.append( str(Path('../UIAutoBaseClass').resolve().absolute()) )
sys.path.append( str(Path('../BugReportGenerator').resolve().absolute()) )

from BugReportGenerator import BugReportGenerator
from UIAutoBaseClass import ChromeTest, ElementFinder

url = "https://gene-drive.bmgf.io/"   
try:
    # find the button with id = close-greeting-modal and click it
    driver = ChromeTest().open_url(url) 
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
    bug_report_generator = BugReportGenerator(e)
    bug_report_generator.generate_bug_report(url, title="Failure in GeneDriveSite")
    
    
finally:
    try:
        driver.save_screenshot("screenshot.png")
    except Exception as screenshot_error:
        print("Failed to capture screenshot:", screenshot_error)
        
    if driver is not None:
        driver.quit()