from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

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