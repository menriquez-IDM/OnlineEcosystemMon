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
        self.chrome_driver_path = '/usr/local/bin/chromedriver'

        if os.name == 'nt':
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
        print('\n** Site URL:', URL)
        if os.path.isfile(self.chrome_driver_path):
            print('Chrome driver found in path:', self.chrome_driver_path)
            # Initialize ChromeDriver service
            service = Service(self.chrome_driver_path)
            # Start the ChromeDriver server
            service.start()

            # Set Chrome options
            chrome_options = Options()
            chrome_options.headless = True
            chrome_options.page_load_strategy = 'eager'
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)

            # Open the website
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.get(URL)
            driver.set_window_size(1920, 1080)
            
            driver.maximize_window()
            # modify the window size
            
            return driver
        else:
            error_message = f'{self.chrome_driver_path}: File does not exist. ' \
                            f'Please make sure you install or download the driver from ' \
                            f'https://chromedriver.chromium.org/downloads'
            raise FileNotFoundError(error_message)



