from pathlib import Path
import os, sys
os.chdir(str(Path(sys.argv[0]).parent))
sys.path.append( str(Path('../UIAutoBaseClass').resolve().absolute()) )
sys.path.append( str(Path('../BugReportGenerator').resolve().absolute()) )
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from UIAutoBaseClass import ChromeTest
from BugReportGenerator import BugReportGenerator

url = "https://leakyvaccine.bmgf.io/"
try:    

    driver = ChromeTest().open_url(url)
    wait = WebDriverWait(driver, 25)

    accept_button = wait.until(EC.element_to_be_clickable((By.ID, "ok")))
    accept_button.click()
    print("Accept button clicked.")   

    # Navigate to Initial example plots tab
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-value='Initial example plots']"))).click()
    print("Initial example plots tab clicked.")
    wait.until(EC.presence_of_element_located((By.ID,"CumulativeInfectionsPlot")))
    wait.until(EC.presence_of_element_located((By.ID,"PlaceboRiskPlot")))
    wait.until(EC.presence_of_element_located((By.ID,"PlaceboVaccineRiskPlot")))
    wait.until(EC.presence_of_element_located((By.ID,"VEPlot")))
    print("PASS: Initial example plots located: CumulativeInfectionsPlot, PlaceboRiskPlot, PlaceboVaccineRiskPlot, VEPlot")
    
    # Navigate to Parameter sweeps tab    
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-value='Parameter sweeps']"))).click()
    print("Parameter sweeps tab clicked.")
    all_plots = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[id^=plotOld]")))
    print("Total charts found: ",  len(all_plots))
    if len(all_plots) != 3:
        raise Exception(f"FAIL:  Expected 3 charts, but found {str(len(all_plots))} charts: \n\n  {all_plots}")    
    print("PASS: Parameter sweeps plots located: plotOld1, plotOld2, plotOld3")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-value='Model fitting']"))).click()
    print("Model fitting tab clicked.")
    wait.until(EC.presence_of_element_located((By.ID,"plotTestLambdaRisk")))
    wait.until(EC.presence_of_element_located((By.ID,"plotTestEspilonRisk")))
    wait.until(EC.presence_of_element_located((By.ID,"plotTestEpsilonLambda")))
    print("PASS: Model fitting plots located: plotTestLambdaRisk, plotTestEspilonRisk, plotTestEpsilonLambda")

    # Model fitting for HVTN 705
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-value='Model fitting for HVTN 705']"))).click()
    print("Model fitting for HVTN 705 tab clicked.")
    wait.until(EC.presence_of_element_located((By.ID,"table1")))
    wait.until(EC.presence_of_element_located((By.ID,"hvtn705distance")))
    print("PASS: Model fitting for HVTN 705 plots located: table1, hvtn705distance")
    
    print("PASS:  LeakyVaccine test completed successfully.")
    
    


except Exception as e:
    print(e)
    print("Exception occurred. Generating bug report...")
    bug_report_generator = BugReportGenerator(e)
    bug_report_generator.generate_bug_report(url, title="LeakyVaccine failed to fully load")
    with open("LeakyVaccine_page_source.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
            
finally:
    try:
        driver.save_screenshot("screenshot.png")
    except Exception as screenshot_error:
        print("Failed to capture screenshot:", screenshot_error)
        
    if driver is not None:
        driver.quit()