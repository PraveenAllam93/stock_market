import streamlit as st
import yfinance as yf


st.title("Stock Market App")

ticker = st.text_input("Enter the ticker of the stock", "AAPL")

ticker_data = yf.Ticker(ticker)
hist = ticker_data.history(period="1mo")

st.write(hist)

st.line_chart(hist["Volume"] )

