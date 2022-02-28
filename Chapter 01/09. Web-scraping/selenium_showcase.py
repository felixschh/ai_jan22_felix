import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


url = "https://www.amazon.es/"
my_driver = "/Users/felixschekerka/Desktop/Strive School/ai_jan22_felix/09. Web-scraping/chromedriver"

driver = webdriver.Chrome(my_driver)
# webdriver.c

driver.get(url)

sleep(3)

#class="a-price-whole"

laptop_price = driver.find_element_by_xpath('//a[@class="a-link-normal a-text-normal"]')

laptop_price.click()

sleep(1)
buy_zone = driver.find_element_by_xpath('//div[@class="a-box-inner"]')


id="price_inside_buybox"
buy_price = buy_zone.find_element_by_xpath('//span[@id="price_inside_buybox"]')

print(buy_price.text)
