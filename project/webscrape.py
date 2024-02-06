#everything found on https://playwright.dev/python/docs
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


#get the URL using response variable
my_url = "https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_technology"
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get(my_url)

response = requests.get(my_url)


soup = BeautifulSoup(browser.page_source, 'html.parser')
browser.close()

lists =[]
