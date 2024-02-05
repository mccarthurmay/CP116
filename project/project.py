

import yfinance as yf
import json, os, pickle

class User_Market:
    def __init__(self, name):
        self.name = name
        self.stocks = {}

    def load_data(self, filename):
            try:
                with open(filename, "rb") as f:  # Open the file in binary read mode ("rb")
                    data = pickle.load(f)
                    self.name = data['user']
                    self.stocks = data['stocks']
                    return True  # Successfully loaded the data
            except (OSError, pickle.UnpicklingError):
                return False  # Failed to load the data

    def save_data(self, filename):
            try:
                with open(filename, "wb") as f:
                    data = {
                        'user': self.name,
                        'stocks': self.stocks
                    }
                    pickle.dump(data, f)
                    print("Profile saved successfully.")
            except OSError:
                print("Failed to save profile.")
    def add_to_stocks(self, symbol):
        y = input(f"How much of {symbol} do you want? ")
        self.stocks[symbol] = int(y)
        print(f"You now have {y} of {symbol}")

    def display_stocks(self):
        print("Stocks in your portfolio:")
        for symbol, quantity in self.stocks.items():
            print(f"{symbol}: {quantity}")


def draw():
    print("##################################")
def clear():
    os.system('clear')






def get_current_price(player, symbol):
    ticker = yf.Ticker(symbol).info
    market_price = ticker['regularMarketOpen']
    previous_close_price = ticker['regularMarketPreviousClose']
    print(f"Ticker: {symbol}")
    print('Market Price:', market_price)
    print('Previous Close Price:', previous_close_price)
    add = input(f"Do you want to add {symbol} to your list? \n")
    if add == 'yes':
        player.add_to_stocks(symbol)
    else:
        print("ok")






def home_screen():
    player = User_Market("")  # Create a default player instance
    if player.load_data("savedata.txt"):
        print("Data loaded successfully.")
        print("Welcome back, " + player.name + "!")
    else:
        name = input("Enter your name: ")
        player = User_Market(name)  # Update the existing instance
    while True:
        clear()
        draw()  # Make sure you have a draw() function defined
        print("# Welcome to NMD Market Insights #")
        draw()  # Make sure you have a draw() function defined
        print("1. Look up a stock \n2. Show your wishlist \n3. Create a Portfolio \n4. Save and exit")
        choice = input("# ")
        if choice == '1':
            tick = input("Enter the Ticker for the Stock \n")
            get_current_price(player, tick)  # Make sure you have get_current_price() function defined
        elif choice == '2':
            player.display_stocks()
            input("#")
        elif choice == '3':
            clear()
        elif choice == '4':
            player.save_data("savedata.txt")
            quit()
        elif choice == '5':
            print(yf.Ticker('GOOGL').info)
            input("#")


input("#")
home_screen()



'''
ticker = yf.Ticker('GOOGL').info
market_price = ticker['regularMarketPrice']
previous_close_price = ticker['regularMarketPreviousClose']
print('Ticker: GOOGL')
print('Market Price:', market_price)
print('Previous Close Price:', previous_close_price)

'''
'''
# get historical market data
hist = msft.history(period="1mo")

# show meta information about the history (requires history() to be called first)
msft.history_metadata

# show actions (dividends, splits, capital gains)
msft.actions
msft.dividends
msft.splits
msft.capital_gains  # only for mutual funds & etfs

# show share count
msft.get_shares_full(start="2022-01-01", end=None)

# show financials:
# - income statement
msft.income_stmt
msft.quarterly_income_stmt
# - balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet
# - cash flow statement
msft.cashflow
msft.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
msft.major_holders
msft.institutional_holders
msft.mutualfund_holders
msft.insider_transactions
msft.insider_purchases
msft.insider_roster_holders

# show recommendations
msft.recommendations
msft.recommendations_summary
msft.upgrades_downgrades

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
msft.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# show news
msft.news

# get option chain for specific expiration
opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
'''
