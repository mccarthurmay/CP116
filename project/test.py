#ask gp to do threadpool analysis
import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression
def volatility_analysis(ticker_list):
    # Add 'SPY' to the list of tickers
    symbols = [ticker, 'SPY']
    data = yf.download(symbols, period = '2y')['Adj Close'] #depending on short term or long term, maybe change years
    #stock prices to daily percent change
    price_change = data.pct_change()
    df = price_change.drop(price_change.index[0])
    # Create arrays for x and y variables in the regression model
    x = np.array(df[ticker]).reshape((-1,1))
    y = np.array(df['SPY'])
    # Define the model and type of regression
    model = LinearRegression().fit(x, y)
    # Prints the beta to the screen
    print('Beta: ', model.coef_)
        volatility_result = volatility_analysis(ticker)
        print("volatility_result")
        #if recommendation_result AND volatility_result == True
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