from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Create ChromeOptions and enable incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Create a new instance of the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://gene-drive.bmgf.io/")

# Define a list of core element locators
element_locators = [
    (By.CSS_SELECTOR, "h1"),  # Example: CSS selector for h1 element
    (By.ID, "example-id"),    # Example: ID of an element
    # Add more locators as needed for other core elements
]

# Validate the presence of each core element
for locator in element_locators:
    try:
        element_present = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        print("Element found:", element_present)
    except:
        print("Element not found:", locator)

# Close the browser
driver.quit()