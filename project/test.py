import tkinter as tk
from tkinter import ttk, simpledialog
import yfinance as yf
import json
import os
import pickle
import warnings
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from functools import partial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from sklearn.linear_model import LinearRegression
import random
import numpy as np


'''
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


'''
'''
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
'''


class User_Market:
    def __init__(self, name):
        self.name = name
        self.stocks = {}

    def load_data(self, filename):
        try:
            with open(filename, "rb") as f:
                data = pickle.load(f)
                self.name = data['user']
                self.stocks = data['stocks']
                return True
        except (OSError, pickle.UnpicklingError):
            return False

    def save_data(self, filename):
            try:
                with open(filename, "wb") as f:
                    data = {
                        'user': self.name,
                        'stocks': self.stocks
                    }
                    pickle.dump(data, f)
            except OSError:
                print("Failed to save profile.")
    def add_to_stocks(self, symbol):
        y = input(f"How much of {symbol} do you want? ")
        self.stocks[symbol] = int(y)




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NMD Market Insights")
        self.geometry("600x400")

        self.player = User_Market("")
        self.load_data()

        self.pages = {}

        self.create_main_page()
        self.create_lookup_page()
        self.create_wishlist_page()
        self.create_portfolio_page()
        self.chrome_options = Options()

        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument('--ignore-ssl-errors')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('log-level=3')


        self.show_page("main")

    def load_data(self):
        if self.player.load_data("savedata.txt"):
            self.welcome_message = f"Data loaded successfully. Welcome back, {self.player.name}!"
        else:
            name = input("Enter your name: ")
            self.player = User_Market(name)
    def scraper(self, sectors):
        ticker_list = []
        for sector in sectors:
            driver = webdriver.Chrome(options=self.chrome_options)

            is_link = 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_' + sector + '?offset=0&count=100'
            driver.get(is_link)

            tickers = driver.find_elements(By.XPATH, '//a[@class="Fw(600) C($linkColor)"]')

            for ticker in tickers:
                ticker_list.append(ticker.text)
            driver.quit()

        return ticker_list

    def fetch_stock_data(self, ticker):
        stock_data = yf.download(ticker, period='5y')
        return stock_data

    def clean_stock_data(self, stock_data):
        cleaned_data = stock_data.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1)
        return cleaned_data

    def recommendation_analysis(self, ticker):
        recommendations = yf.Ticker(ticker).recommendations

        print(f'Ticker: {ticker}, Recommendations:\n{recommendations}')


        if not recommendations.empty:
            buy_count = recommendations.loc[0, 'buy'] + (recommendations.loc[0, 'strongBuy']*1.25)
            sell_count = recommendations.loc[0, 'sell'] + (recommendations.loc[0, 'hold']*.75) + (recommendations.loc[0, 'strongSell']*1.25)
            total_count = buy_count + sell_count

            if total_count > 0:
                positive_percentage = (buy_count / total_count) * 100
                negative_percentage = (sell_count / total_count) * 100

                if positive_percentage - negative_percentage > 40:
                    return True

    def volatility_analysis(self, ticker, stock_data, risk_tolerance):
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
        print('Beta:', model.coef_[0], 'Ticker:', ticker, 'Risk Tolerance:', risk_tolerance)

        if model.coef_ < 1.2 and model.coef_ > 0.8 and risk_tolerance == "medium":
            return True
        elif model.coef_ < 0.8 and risk_tolerance == "low":
            return True
        elif model.coef_ > 1.2 and risk_tolerance == "high":
            return True
        else:
            return False


    def display_portfolio_results(self, results):
        if results:
            result_text = "\n".join([f"{ticker}: {result}" for ticker, result in results.items()])
            self.portfolio_result_label.config(text=result_text, fg="black")
        else:
            self.portfolio_result_label.config(text="No analysis results found.", fg="red")

    def create_main_page(self):
        main_page = ttk.Frame(self)
        main_page.pack(expand=True, fill="both")

        label = tk.Label(main_page, text="Welcome to NMD Market Insights", font=("Helvetica", 14))
        label.pack(pady=10)

        if hasattr(self, 'welcome_message'):
            welcome_label = tk.Label(main_page, text=self.welcome_message, font=("Helvetica", 12), fg="green")
            welcome_label.pack(pady=10)

        lookup_button = ttk.Button(main_page, text="Look up a stock", command=lambda: self.show_page("lookup"))
        lookup_button.pack(pady=10)

        wishlist_button = ttk.Button(main_page, text="Check Wishlist", command=lambda: self.show_page("wishlist"))
        wishlist_button.pack(pady=10)

        portfolio_button = ttk.Button(main_page, text="Create a Portfolio", command=lambda: self.show_page("portfolio"))
        portfolio_button.pack(pady=10)

        save_exit_button = ttk.Button(main_page, text="Save and exit", command=self.save_and_exit)
        save_exit_button.pack(pady=10)

        self.pages["main"] = main_page

    def create_lookup_page(self):
        lookup_page = ttk.Frame(self)
        lookup_page.pack(expand=True, fill="both")

        label = tk.Label(lookup_page, text="Lookup a Stock", font=("Helvetica", 14))
        label.pack(pady=10)

        self.symbol_entry = ttk.Entry(lookup_page)
        self.symbol_entry.pack(pady=10)

        lookup_button = ttk.Button(lookup_page, text="Get Stock Info", command=self.lookup_stock)
        lookup_button.pack(pady=10)

        self.result_label = tk.Label(lookup_page, text="", font=("Helvetica", 12), fg="green")
        self.result_label.pack(pady=10)

        back_button = ttk.Button(lookup_page, text="Back to Main", command=lambda: self.show_page("main"))
        back_button.pack(pady=10)

        self.pages["lookup"] = lookup_page

    def create_wishlist_page(self):
        wishlist_page = ttk.Frame(self)
        wishlist_page.pack(expand=True, fill="both")

        label = tk.Label(wishlist_page, text="Your Wishlist", font=("Helvetica", 14))
        label.pack(pady=10)

        back_button = ttk.Button(wishlist_page, text="Back to Main", command=lambda: self.show_page("main"))
        back_button.pack(pady=10)

        self.canvas = tk.Canvas(wishlist_page, width=5000, height=3000, bg="white")
        self.canvas.pack(pady=10)

        self.pages["wishlist"] = wishlist_page

    def create_portfolio_page(self):
        portfolio_page = ttk.Frame(self)
        portfolio_page.pack(expand=True, fill="both")

        back_button = ttk.Button(portfolio_page, text="Back to Main", command=lambda: self.show_page("main"))
        back_button.pack(pady=10)

        # Update references to use class attributes


        self.portfolio_result_label = tk.Label(portfolio_page, text="", font=("Helvetica", 12), fg="green")
        self.portfolio_result_label.pack(pady=10)

        # Add entry widgets for portfolio inputs
        self.risk_tolerance_entry = ttk.Entry(portfolio_page)
        self.sectors_entry = ttk.Entry(portfolio_page)
        self.impact_investing_entry = ttk.Entry(portfolio_page)
        self.time_horizon_entry = ttk.Entry(portfolio_page)
        self.portfolio_diversification_entry = ttk.Entry(portfolio_page)
        self.investment_amount_entry = ttk.Entry(portfolio_page, text="diversification")

        self.investment_amount_entry.pack(pady=10)

        self.risk_tolerance_entry.pack(pady=10)

        self.sectors_entry.pack(pady=10)

        self.impact_investing_entry.pack(pady=10)

        self.time_horizon_entry.pack(pady=10)

        self.portfolio_diversification_entry.pack(pady=10)

        #self.result_label1 = tk.Label(create_portfolio_page, text="", font=("Helvetica", 12), fg="green")
        #self.result_label1.pack(pady=10)

        # Add a button to trigger the portfolio function
        create_portfolio_button = ttk.Button(portfolio_page, text="Create Portfolio", command=lambda: self.create_portfolio())
        create_portfolio_button.pack(pady=10)

        # Add a label to display the results
        self.portfolio_result_label = tk.Label(portfolio_page, text="", font=("Helvetica", 12), fg="green")
        self.portfolio_result_label.pack(pady=10)

        self.pages["portfolio"] = portfolio_page


    def analysis_dict(self, analysis_results):
        result_text = "Stocks added:\n"
        for ticker, value in analysis_results.items():
            ticker_symbol = ticker.ticker
            result_text += f"{ticker_symbol}:\n"
            for inner_key, inner_value in value.items():
                result_text += f"  {inner_key}: {inner_value}\n"

        if result_text:
            self.portfolio_result_label.config(text=result_text, fg="black")
        else:
            self.portfolio_result_label.config(text="No analysis results found.", fg="red")


    def create_portfolio(self, event=None):
        print("Button clicked!")
        try:
            investment_amount = float(self.investment_amount_entry.get())
            risk_tolerance = self.risk_tolerance_entry.get()
            input_sectors = self.sectors_entry.get().lower()
            sectors = [sector.strip().replace(' ', '-') for sector in input_sectors.split(',')]
            impact_investing = self.impact_investing_entry.get()
            time_horizon = int(self.time_horizon_entry.get())
            portfolio_diversification = self.portfolio_diversification_entry.get()

            user_inputs = {
                "investment_amount": investment_amount,
                "risk_tolerance": risk_tolerance,
                "sectors": sectors,
                "impact_investing": impact_investing,
                "time_horizon": time_horizon,
                "portfolio_diversification": portfolio_diversification
            }

            diversification_levels = {"low": 3, "medium": 5, "high": 10}

            if portfolio_diversification.lower() not in diversification_levels: #changed1
                self.portfolio_result_label.config(text="Invalid portfolio diversification level. Please choose from 'low', 'medium', or 'high'.", fg="red")
                return analysis_results

            ticker_list = self.scraper(sectors)

            # Initialize analysis_results here
            analysis_results = {}  # Add this line

            random.shuffle(ticker_list)
            for ticker in ticker_list:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    stock_data = self.fetch_stock_data(ticker)
                cleaned_data = self.clean_stock_data(stock_data)
                recommendation_result = self.recommendation_analysis(ticker)
                volatility_result = self.volatility_analysis(ticker, stock_data, risk_tolerance)

                min_recommendations = diversification_levels[portfolio_diversification.lower()] #changed1

                if recommendation_result and volatility_result is not None and volatility_result:



                    #calculate where to spread money
                        #grab investment_amount
                        #grab divide by diversification level
                        #ex. user input 3000. 1000 allocated to each stock. Buy as many of the stocks and leave mod.
                    import re
                    ticker = yf.Ticker(ticker)
                    market_price = ticker.info['currentPrice']
                    num_stocks = investment_amount / min_recommendations / market_price
                    b_summary = ticker.info['longBusinessSummary']
                    b_summary = re.split(r'\.\s(?![a-z])', b_summary)
                    b_summary = b_summary[0]



# Take the first sentence

                    #split first sentence
                    analysis_results[ticker] = {
                        #runs through each ticker
                        'Number of Stocks': num_stocks ,
                        'Current Price': market_price ,
                        'Business Summary': b_summary
                        #brief description
                    }



                    if len(analysis_results) >= min_recommendations:


                # Print some debugging information
                        print(num_stocks)
                        print(f"Ticker: {ticker}, Recommendation: {recommendation_result}, Volatility: {volatility_result}")

            # Print the final analysis_results
                        print("Final Analysis Results:", analysis_results)
                        #self.display_portfolio_results(self.analysis_dict(analysis_results))  # Add this line
                        self.analysis_dict(analysis_results)
                        break
        except ValueError as e:
            self.portfolio_result_label.config(text=f"Error: {e}", fg="red")



    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()

        if page_name == "wishlist":
            self.update_wishlist_canvas()
        self.pages[page_name].pack(expand=True, fill="both")

    def lookup_stock(self):
        symbol = self.symbol_entry.get()
        if not symbol:
            self.result_label.config(text="Please enter a valid stock symbol.", fg="red")
            return

        try:
            ticker = yf.Ticker(symbol).info
            market_price = ticker['currentPrice']
            previous_close_price = ticker['regularMarketPreviousClose']
            print(f"Ticker: {symbol}")
            print('Market Price:', market_price)
            print('Previous Close Price:', previous_close_price)

            self.result_label.config(text=f"Symbol: {symbol}\nMarket Price: {market_price}\nPrevious Close Price: {previous_close_price}", fg="black")

            add_to_wishlist = simpledialog.askstring("Add to Wishlist", f"Do you want to add {symbol} to your wishlist? (yes/no)")

            if add_to_wishlist and add_to_wishlist.lower() == 'yes':
                quantity = simpledialog.askfloat("Quantity", f"How much of {symbol} do you want?")
                if quantity is not None:
                    self.player.stocks[symbol] = quantity
                    message = f"Wishlist updated: {symbol} - {quantity} added."
                    self.result_label.config(text=message, fg="green")
                else:
                    self.result_label.config(text="Invalid quantity. Wishlist not updated.", fg="red")
            else:
                self.result_label.config(text="Not added to wishlist.", fg="blue")

        except yf.exceptions.YFinanceException as e:
            message = f"Error fetching data for {symbol}: {e}"
            self.result_label.config(text=message, fg="red")
#For when user clicks on display wishlist
    def update_wishlist_canvas(self):
        self.canvas.delete("all")
        total = len(self.player.stocks)
        if total == 0:
            return

        x_start, y_start = 50, 50
        x_spacing, y_spacing = 300, 250
        max_columns = 3  # Adjust as needed

        for i, (symbol, quantity) in enumerate(self.player.stocks.items()):
            row = i // max_columns
            col = i % max_columns
            x = x_start + col * x_spacing
            y = y_start + row * y_spacing

            bubble_text = self.get_bubble_text(symbol, quantity)
            self.create_bubble(x, y, bubble_text, symbol)

        canvas_width = x_start + max_columns * x_spacing
        canvas_height = y_start + ((total - 1) // max_columns + 1) * y_spacing
        self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))
        self.geometry(f"{canvas_width}x{canvas_height}")

    def get_bubble_text(self, symbol, quantity):
        try:
            ticker = yf.Ticker(symbol)
            current_price = ticker.info.get('regularMarketOpen', 'N/A')
            bubble_text = f"{symbol}\nQuantity: {quantity}\nCurrent Price: {current_price}"
        except yf.exceptions.YFinanceException as e:
            bubble_text = f"{symbol}\nQuantity: {quantity}\nError fetching data: {e}"
        return bubble_text

    def create_bubble(self, x, y, text, symbol):
        bubble = self.canvas.create_oval(x, y, x + 200, y + 200, fill="lightblue", outline="black")
        self.canvas.create_text(x + 100, y + 100, text=text, font=("Helvetica", 10), fill="black")

        button = tk.Button(self.canvas, text="View Graph", command=lambda s=symbol: self.show_stock_graph(s))
        button_window = self.canvas.create_window(x + 100, y + 150, anchor=tk.CENTER, window=button)

    def show_stock_graph(self, symbol):
        try:
            ticker = yf.Ticker(symbol)
            stock_data = ticker.history(period="5y")

            fig, ax = plt.subplots(figsize=(6, 6))
            stock_data['Close'].plot(ax=ax, title=f"{symbol}'s Stock Price")
            plt.show()

        except yf.exceptions.YFinanceException as e:
            message = f"Error fetching data for {symbol}: {e}"
            tk.messagebox.showerror("Error", message)
    def save_and_exit(self):
        self.player.save_data("savedata.txt")
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
