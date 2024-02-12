#You need to have chromedriver.exe in the same folder to run the web scraper

import yfinance as yf
import pandas as pd
import warnings
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import numpy as np
from sklearn.linear_model import LinearRegression
import random

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--headless')
chrome_options.add_argument('log-level=3')
warnings.simplefilter(action='ignore', category=FutureWarning)
def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, period='5y')  #####################################CHANGED####
    return stock_data

def clean_stock_data(stock_data):
    cleaned_data = stock_data.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1)
    return cleaned_data
#####################################CHANGED##########################################
def recommendation_analysis(ticker):
    recommendations = yf.Ticker(ticker).recommendations
    if not recommendations.empty:
        buy_count = recommendations.loc[0, 'buy'] + (recommendations.loc[0, 'strongBuy']*1.25)
        sell_count = recommendations.loc[0, 'sell'] + (recommendations.loc[0, 'hold']*.75) + (recommendations.loc[0, 'strongSell']*1.25)
        total_count = buy_count + sell_count
        if total_count > 0:
            positive_percentage = (buy_count / total_count) * 100
            negative_percentage = (sell_count / total_count) * 100
            if positive_percentage - negative_percentage > 40:
                return True
#basically the code sees the first 10 trues and only prints those, what if we randomized the list then ran this
    return False

#######################CHANGED################################
def volatility_analysis(ticker, stock_data, risk_tolerance):
    # Fetch SPY data for comparison
    spy_data = yf.download('SPY', period='5y')['Adj Close']

    # Concatenate the stock data and SPY data
    data = pd.concat([stock_data['Adj Close'].rename(f"{ticker}"), spy_data.rename('SPY')], axis=1)
    # To standardize data as these two may trade differently
    df = data.pct_change().dropna()

    # Create arrays for x and y variables in the regression model
    x = np.array(df['SPY']).reshape((-1, 1))
    y = np.array(df[ticker])

    # Define the model and type of regression
    model = LinearRegression().fit(x, y)

    # Prints the beta to the screen
    print('Beta:', model.coef_[0], ticker)
    if model.coef_ < 1.2 and model.coef_ > .8 and risk_tolerance == "medium":
        return True
    elif model.coef_ < .8 and risk_tolerance == "low":
        return True
    elif model.coef_ > 1.2 and risk_tolerance == "high":
        return True
    else:
        return False

def scraper(sectors):
    ticker_list = []
    for sector in sectors:
        driver = webdriver.Chrome(options=chrome_options)

        is_link = 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_' + sector + '?offset=0&count=100'
        driver.get(is_link)

        tickers = driver.find_elements(By.XPATH, '//a[@class="Fw(600) C($linkColor)"]')

        for ticker in tickers:
            ticker_list.append(ticker.text)
        driver.quit()

    return ticker_list

def main_analysis(ticker_list, portfolio_diversification, investment_amount):
    analysis_results = {}

    diversification_levels = {"low": 3, "medium": 5, "high": 10}

    if portfolio_diversification.lower() not in diversification_levels:
        print("Invalid portfolio diversification level. Please choose from 'low', 'medium', or 'high'.")
        return analysis_results

    min_recommendations = diversification_levels[portfolio_diversification.lower()]

    # Adjust min_recommendations based on investment amount
    if investment_amount > 1000:
        min_recommendations += 1
    random.shuffle(ticker_list) #####Randomize data... would be better if we compared all analyst ratings and sorted by that######CHANGED####
    for ticker in ticker_list:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            stock_data = fetch_stock_data(ticker)
        cleaned_data = clean_stock_data(stock_data)
        recommendation_result = recommendation_analysis(ticker)
        volatility_result = volatility_analysis(ticker, stock_data, risk_tolerance) #####################################CHANGED####
        if recommendation_result and volatility_result == True: #####################################CHANGED####
            analysis_results[ticker] = {
                'Recommendation Analysis': recommendation_result,
                'Volatility Result': volatility_result
            }

            if len(analysis_results) >= min_recommendations:
                break

    return analysis_results

while input != 'quit':

    sectors = []
    investment_amount = float(input("Enter your investment amount: "))
    risk_tolerance = input("Enter your risk tolerance (high, medium, low): ")
    input_sectors = input("Input sectors (comma-separated): ").lower()
    impact_investing = input("Are you interested in impact investing? (yes/no): ")
    time_horizon = int(input("Enter your time horizon (in months): "))
    portfolio_diversification = input("Enter desired portfolio diversification (if not provided, we'll use random): ")
    user_inputs = {
        "investment_amount": investment_amount,
        "risk_tolerance": risk_tolerance,
        "sectors": sectors,
        "impact_investing": impact_investing,
        "time_horizon": time_horizon,
        "portfolio_diversification": portfolio_diversification
    }
    for sector in input_sectors.split(','):
        sectors.append(sector.strip().replace(' ', '-'))

    ticker_list = scraper(sectors)
    results = main_analysis(ticker_list, portfolio_diversification, investment_amount)
    print(results)



"""
Beta = 1:
A beta of 1 indicates that the stock tends to move in line with the benchmark.
 If the benchmark goes up by 5%, the stock, on average, is expected to go up by 5%,
 and vice versa.
 - middle ground

Beta > 1:
A beta greater than 1 suggests that the stock is more volatile than the market.
 If the benchmark goes up by 1%, a stock with a beta greater than 1 is expected
 to have a larger percentage increase, and similarly, it would experience a larger decline if the market falls.
 - higher returns, increased risks

Beta < 1:
A beta less than 1 implies that the stock is less volatile than the market.
If the benchmark goes up by 1%, a stock with a beta less than 1 is expected to
have a smaller percentage increase, and it would likely experience a smaller decline if the market falls.
- stable investment, lower returns

Beta = 0:
A beta of 0 suggests that the stock's price movements are not correlated with the
benchmark. In other words, changes in the market do not predictably influence the
stock's performance.
- no systematic risk

Negative Beta:
In rare cases, a stock may have a negative beta. A negative beta implies an inverse
relationship with the benchmark. If the market goes up, a stock with a negative beta
might be expected to go down, and vice versa. This is often associated with assets that tend to move counter to the overall market, such as certain gold stocks.
- hedge against market downturns
"""
