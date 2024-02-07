import yfinance as yf
import pandas as pd
import warnings #allows code to run even with warnings

investment_amount = float(input("Enter your investment amount: "))
risk_tolerance = input("Enter your risk tolerance (high, medium, low): ")
sector = input("Enter the sector(s) of interest: ")
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

def portfolio_diversification(portfolio_diversification):
    print("nothing")
    #if input_pd == "low"
        #return 3
    #if input_pd == "medium"
        #return 5
    #if input_pd == "high"
        #return 10
def time_horizon(time_horizon):
    #filter good short term, medium term, long term



def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, start='2020-01-01', end='2023-02-01')  # adjust dates range as needed
    return stock_data

def clean_stock_data(stock_data):
    cleaned_data = stock_data.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1) #need to do more to clean data
    return cleaned_data


def recommendation_analysis(ticker):
    recommendations = yf.Ticker(ticker).recommendations
    if not recommendations.empty:
        if 'To Grade' in recommendations.columns:
            positive_signals = ['Buy', 'Strong Buy']
            negative_signals = ['Hold', 'Sell', 'Strong Sell']

            buy_count = recommendations[recommendations['To Grade'].isin(positive_signals)].shape[0]
            sell_count = recommendations[recommendations['To Grade'].isin(negative_signals)].shape[0]
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

        analysis_results[ticker] = {
            'Recommendation Analysis': recommendation_result
        }

    return analysis_results


# Example tickers:
user_input_tickers = ['AAPL', 'GOOGL', 'MSFT']
results = main_analysis(user_input_tickers)
print(results)
