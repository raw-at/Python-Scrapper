from selenium import webdriver
import bs4 as bs
import lxml
import requests
path_to_chrome = '/home/brutal/Desktop/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chrome)
url = 'https://www.walmart.com/cp/1078664'
browser.get(url)


browser.find_element_by_id('left').click()
