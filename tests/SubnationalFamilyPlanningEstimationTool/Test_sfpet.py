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

    driver.implicitly_wait(15)

    # Main Map
    chart1 = driver.find_element(By.ID, "chart1")
    driver.implicitly_wait(25)
    if chart1:  print("PASS:  Main Map exists.")
    else: print("Main Map (chart1) does not exist.")
    driver.implicitly_wait(25)
    
    # Comparison map    
    chart2= driver.find_element(By.ID, "chart2")
    driver.implicitly_wait(25)
    if chart2:  print("PASS:  Comparison Map exists.")
    else: print("Comparison map (chart2) does not exist.")
    driver.implicitly_wait(25)
    
    # Women 15-24 
    chart68 = driver.find_element(By.ID, "chart68")
    driver.implicitly_wait(25)
    if chart68:  print("PASS:  Women 15-24 chart exists.")
    else: print("Women 15-24 (chart68) does not exist.")
    
    
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