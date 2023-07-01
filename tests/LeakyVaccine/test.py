from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
# Path to ChromeDriver executable
chrome_driver_path = '/usr/local/bin/chromedriver'

# verify if the file exists
if os.path.isfile(chrome_driver_path):
    print('File exists')
    

    # Initialize ChromeDriver service
    service = Service(chrome_driver_path)
    # Start the ChromeDriver server
    service.start()

    # Set Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--incognito")

    # Open the website
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://leakyvaccine.bmgf.io/")
    driver.implicitly_wait(2)
    privacy_banner = driver.find_element(By.ID, "ok")
    privacy_banner.click()
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

    # Close the browser
    driver.quit()

else:
    print('File does not exist')
    