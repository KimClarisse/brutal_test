import unittest
from selenium import webdriver

class TestBrutal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = r"C:\Users\Ayame\Documents\Python\geckodriver.exe")

    def test_title(self):
        self.driver.get("https://aloisdegouvello.gitlab.io/brutal/index.html")

        page_title = self.driver.title

        self.assertEqual(page_title, 'Brutal')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
     unittest.main()