import numpy as np 
import pandas as pd
import seaborn as sns 
import streamlit as st
import yfinance as yf

st.write("""
         ## Simple Stock Price App
         
         Shown are the stock closing price and volume of Google!

         """)
tickersymbol = 'AAPL'

tickerData =yf.Ticker(tickersymbol)

tickerdf =  tickerData.history(period="1d", start="2020-01-01",end='2023-08-01')
st.write("""
### Closing Price
""")
st.line_chart(tickerdf["Close"])

st.write("""
### Total Volume
""")
st.line_chart(tickerdf["Volume"])
st.write(tickerdf)



