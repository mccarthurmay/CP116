import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, period='5y')
    return stock_data

def volatility_analysis(ticker, stock_data):
    # Fetch SPY data for comparison
    spy_data = yf.download('SPY', period='5y')['Adj Close']

    # Concatenate the stock data and SPY data
    data = pd.concat([stock_data['Adj Close'].rename(f"{ticker}"), spy_data.rename('SPY')], axis=1)
    # To standardize data as these two may trade differently
    print(data)
    df = data.pct_change().dropna()
    print(df)

    # Create arrays for x and y variables in the regression model
    x = np.array(df['SPY']).reshape((-1, 1))
    y = np.array(df[ticker])
    print(x)
    print(y)
    # Define the model and type of regression
    model = LinearRegression().fit(x, y)

    # Prints the beta to the screen
    print('Beta:', model.coef_[0])
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
                return print(True)
#basically the code sees the first 10 trues and only prints those, what if we randomized the list then ran this
    return print(False)
# Get user input for the ticker symbol
t = "1"
while t != "2":
    ticker = input("Enter ticker symbol: ")
    stock_data = fetch_stock_data(ticker)
    volatility_analysis(ticker, stock_data)
    recommendation_analysis(ticker)





"""
Beta = 1:
A beta of 1 indicates that the stock tends to move in line with the benchmark.
 If the benchmark goes up by 1%, the stock, on average, is expected to go up by 1%,
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
