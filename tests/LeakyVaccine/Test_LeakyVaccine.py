from pathlib import Path
import os, sys
os.chdir(str(Path(sys.argv[0]).parent))
sys.path.append( str(Path('../UIAutoBaseClass').resolve().absolute()) )
sys.path.append( str(Path('../BugReportGenerator').resolve().absolute()) )

from selenium.webdriver.common.by import By
from UIAutoBaseClass import ChromeTest
from BugReportGenerator import BugReportGenerator

url = "https://leakyvaccine.bmgf.io/"
try:    
    driver = ChromeTest().open_url(url)
    driver.implicitly_wait(2)

    driver.find_element(By.ID, "ok").click()

    #sleep for 5 seconds
    driver.implicitly_wait(2)

    # Navigate to Initial example plots tab
    driver.find_element(By.CSS_SELECTOR, "a[data-value='Initial example plots']").click()
    driver.implicitly_wait(8)

    # Find the cumulative infections plot element
    cumulative_infections_plot = driver.find_element(By.ID, "CumulativeInfectionsPlot")
    driver.implicitly_wait(8)

    # Verify that the cumulative infections plot exists
    if cumulative_infections_plot:  print("PASS:  Cumulative infections plot exists.")
    else: print("Cumulative infections plot does not exist.")
    driver.implicitly_wait(8)

    # Navigate to Parameter sweeps tab
    driver.find_element(By.CSS_SELECTOR, "a[data-value='Parameter sweeps']").click()
    driver.implicitly_wait(15)

    # data-subplot = 'x2y'
    plotx2y = driver.find_element(By.CSS_SELECTOR, "rect[data-subplot='x2y']")
    if plotx2y:  print("PASS:  plotx2y exists.")
    else: print("plotx2y does not exist.")
    
    print("PASS:  LeakyVaccine test completed successfully.")

except Exception as e:
    print(e)
    print("Exception occurred. Generating bug report...")
    bug_report_generator = BugReportGenerator(e)
    bug_report_generator.generate_bug_report(url, title="LeakyVaccine Page 1 and Page 2 failed to load")
    
finally:
    try:
        driver.save_screenshot("screenshot.png")
    except Exception as screenshot_error:
        print("Failed to capture screenshot:", screenshot_error)
        
    if driver is not None:
        driver.quit()