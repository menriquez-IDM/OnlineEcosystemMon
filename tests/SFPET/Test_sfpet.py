from pathlib import Path
import os, sys, time
os.chdir(str(Path(sys.argv[0]).parent))
sys.path.append( str(Path('../UIAutoBaseClass').resolve().absolute()) )
sys.path.append( str(Path('../BugReportGenerator').resolve().absolute()) )

from selenium.webdriver.common.by import By
from selenium import webdriver
from UIAutoBaseClass import ChromeTest
from BugReportGenerator import BugReportGenerator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://sfpet.bmgf.io/"
try:    
    driver = ChromeTest().open_url(url)
    wait = WebDriverWait(driver, 25)

    accept_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    accept_button.click()
    print("Accept button clicked.")   
    
    all_charts = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[id^=chart]")))
    print("Total charts found: ",  len(all_charts))

    if len(all_charts) != 15:
        raise Exception(f"FAIL:  Expected 15 charts, but found {str(len(all_charts))} charts: \n\n  {all_charts}")
    else:
        for chart in all_charts: 
            print("Found Chart: ", chart.get_attribute("id"))
        print("Clicking on the Main and Comparison maps ...")
        all_charts[0].click()   
        all_charts[1].click()   
        
        print("PASS:  Subnational Family Planning Estimation Tool test completed successfully.")
    
except Exception as e:
    print(e)
    print("Exception occurred. Generating bug report...")
    bug_report_generator = BugReportGenerator(e)
    bug_report_generator.generate_bug_report(url, title="Subnational Family Planning Estimation Tool Failed to fully load")
    
finally:
    try:
        driver.save_screenshot("screenshot.png")
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
            
    except Exception as screenshot_error:
        print("Failed to capture screenshot:", screenshot_error)
        
    if driver is not None:
        driver.quit()