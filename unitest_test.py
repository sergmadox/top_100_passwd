import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

class GooogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_search_in_google(self):
        
        driver = self.driver
        driver.get('https://google.com')
        elem = driver.find_element_by_name('q')
        elem.send_keys('Python')
        elem.send_keys(Keys.RETURN)
        elemnet = WebDriverWait(driver,10000).until(driver.find_element_by_xpath("//*[@id='hdtb-msb-vis']/div[2]/a"))
        #elem2 = driver.find_element_by_xpath("//*[@id='hdtb-msb-vis']/div[2]/a");
        elemnet.click()

        assert "No results found." not in driver.page_source
    
    def close(self):
        self.driver.close()
        
if __name__ == '__test_search_in_google__':
    unittest.main()
    