import streamlit as st
import pandas as pd
import yfinance as yf

stocks = ('AAPL','ADBE','AMZN','ASML','AVGO',
           'CMCSA','COST','CSCO','FB','GOOG','GOOGL',
           'INTC','MSFT','NFLX','NTES','NVDA','PEP',
           'PYPL','QCOM','TSLA')

st.title('Stock dashboard for the companies with Mega market cap')

stock_choice = st.multiselect('Choose the stock',stocks)
startdate = st.date_input('Start date',value = pd.to_datetime('2011-01-01'))
enddate = st.date_input('End date',value = pd.to_datetime('today'))


if len(stock_choice)>0 :
    st.write('Adjusted close price from Yahoo Finance API')
    df=yf.download(stock_choice,startdate,enddate)['Adj Close']
    st.line_chart(df)

