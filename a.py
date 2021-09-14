from selene.support.shared import browser
from selene import by, be, have

from selenium.webdriver import Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True

driver = Chrome(desired_capabilities=capabilities, executable_path=r'C:\chromedriver.exe')
browser.set_driver(driver)

browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank)\
    .type('selenium').press_enter()
browser.all('.g').should(have.size(16))\
    .first.should(have.text('Selenium automates browsers'))

