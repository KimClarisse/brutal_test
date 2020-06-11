import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        

def check_exists_by_css(driver, selector):
    try:
        driver.find_element_by_css_selector(selector)
    except NoSuchElementException:
        return False
    return True

class TestBrutal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = r"C:\Users\Ayame\Documents\Python\geckodriver.exe")

    def test_title(self):
        self.driver.get("https://aloisdegouvello.gitlab.io/brutal/index.html")

        page_title = self.driver.title

        self.assertEqual(page_title, 'Brutal')

    def test_check_exists_header(self):
        self.driver.get("https://aloisdegouvello.gitlab.io/brutal/index.html")

        selector = "#app header img" 
        does_exist = check_exists_by_css(self.driver, selector)

        self.assertTrue(does_exist, "Header's image not found.")

    def test_check_exists_bba(self):
        self.driver.get("https://aloisdegouvello.gitlab.io/brutal/index.html")

        selector = "#inline-bba" 
        does_exist = check_exists_by_css(self.driver, selector)

        self.assertTrue(does_exist, "BBA input not found.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
     unittest.main()