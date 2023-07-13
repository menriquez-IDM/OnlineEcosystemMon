from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class ChromeTest:
    def __init__(self):
        """
        Initializes the ChromeTest class.
        Sets the path for the ChromeDriver based on the operating system.
        """
        if os.name == "linux":
            self.chrome_driver_path = '/usr/local/bin/chromedriver'

        else:
            self.script_path = os.path.dirname(os.path.realpath(__file__))
            self.chrome_driver_path = os.path.join(self.script_path, 'chromedriver.exe')
            # add the curren directory to the PYTHONPATH


    def open_url(self, URL):
        """
        Opens the specified URL in headless Chrome browser.

        Args:
            URL (str): The URL to open in the browser.

        Returns:
            selenium.webdriver.Chrome: The Chrome WebDriver instance.

        Raises:
            FileNotFoundError: If the ChromeDriver executable file is not found.
        """
        if os.path.isfile(self.chrome_driver_path):
            print('Chrome driver found in path:', self.chrome_driver_path)
            # Initialize ChromeDriver service
            service = Service(self.chrome_driver_path)
            # Start the ChromeDriver server
            service.start()

            # Set Chrome options
            chrome_options = Options()
            chrome_options.headless = True
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)

            # Open the website
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.get(URL)
            return driver
        else:
            error_message = f'{self.chrome_driver_path}: File does not exist. ' \
                            f'Please make sure you install or download the driver from ' \
                            f'https://chromedriver.chromium.org/downloads'
            raise FileNotFoundError(error_message)



class ElementFinder:
    """
    A base class that finds an element using a specified locator and exposes its capabilities.
    """

    def __init__(self, locator, locator_value):
        """
        Initialize the ElementFinder.

        Args:
            locator (selenium.webdriver.common.by): The locator strategy to find the element.
            locator_value (str): The value associated with the locator strategy.
        """
        self.locator = locator
        self.locator_value = locator_value

    def find_element(self, driver):
        """
        Find the element using the specified locator and locator value.

        Args:
            driver (selenium.webdriver.WebDriver): The WebDriver instance to use for finding the element.

        Returns:
            selenium.webdriver.remote.webelement.WebElement: The found WebElement.
        """
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((self.locator, self.locator_value))
        )
        return element

    def expose_capabilities(self, element):
        """
        Expose the capabilities of the element by printing its attributes.

        Args:
            element (selenium.webdriver.remote.webelement.WebElement): The WebElement whose capabilities will be exposed.
        """
        print(f"Element with locator {self.locator} and value '{self.locator_value}' has the following capabilities:")
        print(f"Text: {element.text}")
        print(f"Tag Name: {element.tag_name}")
        print(f"Is Enabled: {element.is_enabled()}")
        print(f"Is Displayed: {element.is_displayed()}")
        print(f"Location: {element.location}")
        print(f"Size: {element.size}")

    def find_and_expose(self, driver):
        """
        Find the element and expose its capabilities.

        Args:
            driver (selenium.webdriver.WebDriver): The WebDriver instance to use for finding the element.
        """
        element = self.find_element(driver)
        self.expose_capabilities(element)
        print(f"Element with locator {self.locator} and value '{self.locator_value}' was found.")

