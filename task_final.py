from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://google.com/ncr')

# steps 1 to 3
input = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input.send_keys('selenide')
input.send_keys(Keys.RETURN)
firstUrl = driver.find_element_by_tag_name('cite')
assert 'selenide.org' in firstUrl.text

# steps 4, 5
images = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
images.send_keys(Keys.RETURN)
imageContent = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]')
assert 'selenide.org' in imageContent.text

# steps 6, 7
backToAll = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
backToAll.send_keys(Keys.RETURN)
firstUrlAgain = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite')
assert 'selenide.org' in firstUrlAgain.text

driver.close()