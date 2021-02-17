# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:19:08 2021

@author: shubh
"""


import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of your specified company
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
tickerSymbol=st.text_area("Enter NASDAQ Company ID", tickerSymbol, height=10)
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""## Opening Price """)
st.line_chart(tickerDf.Open)
st.write("""## Closing Price """)
st.line_chart(tickerDf.Close)
st.write("""## Volume Price """)
st.line_chart(tickerDf.Volume)
st.write("""## Dividends """)
st.line_chart(tickerDf.Dividends)