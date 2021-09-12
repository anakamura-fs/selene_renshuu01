from selene.support.shared import browser
from selene import by, be, have

browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank)\
    .type('selenium').press_enter()
browser.all('.g').should(have.size(16))\
    .first.should(have.text('Selenium automates browsers'))

