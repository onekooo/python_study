#use xpass and css  selector login to github.com
from selenium import webdriver
import time
try:
    # driver = webdriver.Chrome('C:/Users/sj/Downloads/chromedriver.exe')
    # driver = webdriver.Chrome('C:/Users/YG/Downloads/chromedriver.exe')
    driver=webdriver.Chrome('D:/python37/Scripts/chromedriver.exe')
    driver.get('https://github.com/future1012/')
    time.sleep(2)
    print('Title:',driver.title)
    print('Current url:',driver.current_url)
    driver.refresh()
    driver.maximize_window()
    time.sleep(2)
    driver.minimize_window()
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@class='HeaderMenu-link no-underline mr-3']").click()
    time.sleep(2)
    driver.find_element_by_css_selector("#login_field").send_keys("tengyue1023@163.com")
    time.sleep(2)
    driver.find_element_by_css_selector("#password").send_keys("xxxxxx")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@value='Sign in']").click()
    time.sleep(2)
    driver.get("https://www.google.com")
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    print(driver.page_source)
    driver.close()
except:
    print('login failed')
