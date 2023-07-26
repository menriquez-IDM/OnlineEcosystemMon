from pathlib import Path
import os, sys
os.chdir(str(Path(sys.argv[0]).parent))
sys.path.append( str(Path('../UIAutoBaseClass').resolve().absolute()) )
sys.path.append( str(Path('../BugReportGenerator').resolve().absolute()) )

from selenium.webdriver.common.by import By
from UIAutoBaseClass import ChromeTest
from BugReportGenerator import BugReportGenerator

url = "https://sfpet.bmgf.io/"
try:    
    driver = ChromeTest().open_url(url)
    driver.implicitly_wait(5)

    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

    driver.implicitly_wait(10)

    # Find the chart1 element
    chart1 = driver.find_element(By.ID, "chart1")
    driver.implicitly_wait(15)
    if chart1:  print("PASS:  chart1 exists.")
    else: print("chart1 does not exist.")

    # If it reaches this point, then report as successful    
    print("PASS:  Subnational Family Planning Estimation Tool test completed successfully.")

except Exception as e:
    print(e)
    print("Exception occurred. Generating bug report...")
    bug_report_generator = BugReportGenerator(e)
    bug_report_generator.generate_bug_report(url, title="Subnational Family Planning Estimation Tool Failed to fully load")
    
finally:
    try:
        driver.save_screenshot("screenshot.png")
    except Exception as screenshot_error:
        print("Failed to capture screenshot:", screenshot_error)
        
    if driver is not None:
        driver.quit()