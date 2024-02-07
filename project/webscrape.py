import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--headless')

chrome_options.add_argument('log-level=3')

#scraper function
def scraper():

    #set webdriver to chrome
    driver = webdriver.Chrome(options = chrome_options)

    is_link ='https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_' + sector + '?offset=0&count=100'


    driver.get(is_link)

    tickers = driver.find_elements(By.XPATH, '//a[@class="Fw(600) C($linkColor)"]')
    ticker_list = []
    for ticker in tickers:
        ticker_list.append(ticker.text)

    driver.quit()
    print (ticker_list)

######TEMPORARY DEFINITION#####
print("Technology, Financial Services, Healthcare, Consumer Cyclical, Industrials, Communication Services, Consumer Defensive, Energy, Basic Materials, Real Estate, Utilities")
######TEMPORARY INPUT#####
while input != 'quit':
    sector = input("Input sector: ").lower().strip()
    if sector == "financial services":
        sector = "financial-services"
    elif sector == "consumer cyclical":
        sector = "consumer-cyclical"
    elif sector == "communication services":
        sector = "communication-services"
    elif sector == "consumer defensive":
        sector = "consumer-defensive"
    elif sector == "basic materials":
        sector = "basic-materials"
    elif sector == "real estate":
        sector = "real-estate"
    scraper()
