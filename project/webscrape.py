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
def scraper(sectors):

    for sector in sectors:
        ticker_list = []
        driver = webdriver.Chrome(options = chrome_options)

        is_link ='https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_' + sector + '?offset=0&count=100'


        driver.get(is_link)

        tickers = driver.find_elements(By.XPATH, '//a[@class="Fw(600) C($linkColor)"]')

        for ticker in tickers:
            ticker_list.append(ticker.text)

        driver.quit()
        sus_scrape(ticker_list)
        print(sus_ticker_list)


    #set webdriver to chrome
def sus_scrape(ticker_list):
    for ticker in ticker_list:
        sus_ticker_list = []
        sus_driver = webdriver.Chrome(options = chrome_options)
        sus_link ='https://finance.yahoo.com/quote/'+ticker+'/sustainability?p='+ticker
        sus_driver.get(sus_link)

        sus_tickers = sus_driver.find_elements(By.XPATH, '//div[@class="D(ib) Fz(23px) smartphone_Fz(22px) Fw(600)"]')
        for sus_ticker in sus_tickers:
            sus_ticker_list.append(sus_ticker.text)



######TEMPORARY DEFINITION#####
print("Technology, Financial Services, Healthcare, Consumer Cyclical, Industrials, Communication Services, Consumer Defensive, Energy, Basic Materials, Real Estate, Utilities")
######TEMPORARY INPUT#####
while input != 'quit':
    input_sectors = input("Input sectors (comma-separated): ").lower()
    sectors = []

    for sector in input_sectors.split(','):
        sectors.append(sector.strip().replace(' ', '-'))
    scraper(sectors)
