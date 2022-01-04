import streamlit as st
import pandas as pd
import yfinance as yf

stocks = ('AAPL','ADBE','AMZN','ASML','AVGO',
           'CMCSA','COST','CSCO','FB','GOOG','GOOGL',
           'INTC','MSFT','NFLX','NTES','NVDA','PEP',
           'PYPL','QCOM','TSLA')

st.title('Stock dashboard')

stock_choice = st.multiselect('Choose the stock for the companies with Mega market cap',stocks)
if len(stock_choice)== 0:
    stock_choice = st.text_input ('Or you can input your own stock ticker symbol')
startdate = st.date_input('Start date',value = pd.to_datetime('2012-01-01'))
enddate = st.date_input('End date',value = pd.to_datetime('today'))


if len(stock_choice)>0 :
    st.write('Adjusted close price')
    df=yf.download(stock_choice,startdate,enddate)['Adj Close']
    st.line_chart(df)
