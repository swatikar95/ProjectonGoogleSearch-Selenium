from selenium import webdriver
import unittest
import HtmlTestRunner

class GoggleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")
        # cls.driver.get("https://google.com")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_search(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("btnK").click()


    def test_search1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("What is SQA")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Process is complete")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C://Users/HP/Google Drive/Learning/ProjectonGoogleSearch/report"))



