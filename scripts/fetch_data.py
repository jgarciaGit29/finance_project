# Get data from Yahoo Fiance
import yfinance as yahooFinance
import pandas as pd
ticker = yahooFinance.Ticker('TSLA')
history = ticker.history(period="max")  # You can specify the period (e.g., "1y", "5d", "max")

#Convert the dictinory to a dataframe and Transposing with .T
history.to_csv(r'data/raw/Tesla_Historical_Data.csv',index=True)
print("Tesla historical data has been saved to data/raw/Tesla_Historical_Data.csv")
