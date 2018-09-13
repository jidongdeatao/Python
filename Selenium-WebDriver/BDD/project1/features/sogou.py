#encoding=utf-8
from lettuce import *
from selenium import webdriver
import time

@step('I have the english name "(.*)"')
def have_the_searchWord(step,searchWord):
    world.searchWord = str(searchWord)
    print world.searchWord

@step('I search it in Sougou website')
def search_in_sougou_website(step):
    world.driver = webdriver.Firefox()
    world.driver.get('http://www.sogou.com')
    world.driver.find_element_by_id("query").send_keys(world.searchWord)
    world.driver.find_element_by_id("stb").click()
    time.sleep(3)

@step('I see the entire name "(.*)"')
def check_result_in_sougou(step,searchResult):
    assert searchResult in world.driver.page_source," got word: %s"%searchResult
    world.driver.quit()
