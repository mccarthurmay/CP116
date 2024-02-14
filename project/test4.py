import pprint
import yfinance as yf
def print_inventory(dct):
    print("Items held:")
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print("{} ({})".format(item, amount))

inventory = {
    "shovels": 3,
    "sticks": 2,
    "dogs": 1,
}
print_inventory(inventory)
ticker = yf.Ticker('GM')
market_price = ticker.info['currentPrice']

b_summary = ticker.info['longBusinessSummary']
b_summary = b_summary.split('.')
b_summary = b_summary[0]

print(b_summary)
