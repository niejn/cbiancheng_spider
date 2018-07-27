from selenium import webdriver
options = webdriver.FirefoxOptions()
options.set_headless()
# options.add_argument(‘-headless‘)
# options.add_argument('--disable-gpu')
driver=webdriver.Firefox(firefox_options=options)
driver.get('http://httpbin.org/user-agent')
driver.get_screenshot_as_file('test.png')
driver.close()

from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180309/FutureDataHolding.htm")

sleep(1000)