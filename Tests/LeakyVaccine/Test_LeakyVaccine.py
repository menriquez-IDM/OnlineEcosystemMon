from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create ChromeOptions and enable incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Create a new instance of the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options, executable_path="..\\chromedriver.exe")

# Open the website
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

