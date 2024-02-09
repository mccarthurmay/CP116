import yfinance as yf
import pandas as pd
import warnings #allows code to run even with warnings
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
####################################
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--headless')
chrome_options.add_argument('log-level=3')

def p_d(portfolio_diversification):
    print("nothing")
    #if input_pd == "low"
        #return 3
    #if input_pd == "medium"
        #return 5
    #if input_pd == "high"
        #return 10
#def time_horizon(time_horizon):
    #filter good short term, medium term, long term

def i_i(impact_investing):
    print("nothing")
    #loop through each ticker and assign ESG rating from scraped results

#############################################
#not changed


def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, start='2020-01-01', end='2023-02-01')  # adjust dates range as needed
    return stock_data

def clean_stock_data(stock_data):
    cleaned_data = stock_data.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1) #need to do more to clean data
    return cleaned_data

################################################
#changed
def recommendation_analysis(ticker):
    recommendations = yf.Ticker(ticker).recommendations
    if not recommendations.empty:
        #Added weights (strong = 1.1x, hold = .75x, buy/sell = 1x)
        buy_count = recommendations.loc[0, 'buy'] + (recommendations.loc[0, 'strongBuy']*1.1)
        sell_count = recommendations.loc[0, 'sell'] + (recommendations.loc[0, 'hold']*.75) + (recommendations.loc[0, 'strongSell']*1.1)
        positive_signals = ['buy', 'strongBuy']
        negative_signals = ['hold', 'sell', 'strongSell']

        total_count = recommendations.shape[0]

        if total_count > 0:
            positive_percentage = (buy_count / total_count) * 100
            negative_percentage = (sell_count / total_count) * 100
            if positive_percentage - negative_percentage > 3:
                return True

    return False


def main_analysis(ticker_list):
    analysis_results = {}

    for ticker in ticker_list:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            stock_data = fetch_stock_data(ticker)
        cleaned_data = clean_stock_data(stock_data)
        recommendation_result = recommendation_analysis(ticker)
        #only return True results
        if recommendation_result == True:
            analysis_results[ticker] = {
                'Recommendation Analysis': recommendation_result
            }

    return analysis_results

def scraper(sectors):
    ticker_list = []
    for sector in sectors:
        driver = webdriver.Chrome(options = chrome_options)

        is_link ='https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_' + sector + '?offset=0&count=100'


        driver.get(is_link)

        tickers = driver.find_elements(By.XPATH, '//a[@class="Fw(600) C($linkColor)"]')

        for ticker in tickers:
            ticker_list.append(ticker.text)
        driver.quit()

    return ticker_list


while input != 'quit':
    investment_amount = float(input("Enter your investment amount: "))
    risk_tolerance = input("Enter your risk tolerance (high, medium, low): ")
    input_sectors = input("Input sectors (comma-separated): ").lower()
    sectors = []
    for sector in input_sectors.split(','):
        sectors.append(sector.strip().replace(' ', '-'))
    impact_investing = input("Are you interested in impact investing? (yes/no): ")
    time_horizon = int(input("Enter your time horizon (in months): "))
    portfolio_diversification = input("Enter desired portfolio diversification (if not provided, we'll use random): ")
    user_inputs = {
        "investment_amount": investment_amount,
        "risk_tolerance": risk_tolerance,
        "sector": sector,
        "impact_investing": impact_investing,
        "time_horizon": time_horizon,
        "portfolio_diversification": portfolio_diversification
    }
    ticker_list = scraper(sectors)
    results = main_analysis(ticker_list)
    print(results)
######################################
