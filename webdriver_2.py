import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):

    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return


chromedriver = 'D:\chromedriver\chromedriver.exe'
# driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver = webdriver.Chrome(executable_path='D:\chromedriver\chromedriver.exe')
driver.get('http://vip.biancheng.net/login.php')
# driver = webdriver.Chrome()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("niejn")
password.send_keys("cxf8922470")

driver.find_element_by_name("submit").click()
waitForLoad(driver)
# time.sleep(3) # Let the user actually see something!


driver.get('http://c.biancheng.net/cpp/biancheng/view/3010.html')
print(driver.page_source)
print(driver.get_cookies())
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()