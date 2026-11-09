
# AC420 Assignment 5
# Created by GiBeom Kim

# Import necessary packages
import streamlit as st
import yfinance as yf
import pandas as pd

# Title of the Streamlit App
st.title("Microsoft (MSFT) Sharpe Ratio by GiBeom Kim")

# Define the stock ticker and risk-free rate
ticker = "MSFT"
rf_monthly = 0.0025  # 0.25% per month

# Download 5 years of monthly stock data
data = yf.Ticker(ticker).history(
    period="5y",
    interval="1mo"
)

# Check whether stock data is available
if not data.empty:

    # Extract closing prices
    close_prices = data["Close"]

    # Calculate monthly stock returns
    monthly_returns = close_prices.pct_change().dropna()

    if len(monthly_returns) >= 2:

        # Calculate monthly excess returns
        excess_returns = monthly_returns - rf_monthly

        # Calculate average excess return
        mean_excess_return = excess_returns.mean()

        # Calculate standard deviation
        std_dev_return = monthly_returns.std()

        if std_dev_return > 0:

            # Calculate monthly Sharpe Ratio
            monthly_sharpe_ratio = (
                mean_excess_return / std_dev_return
            )

            # Display result on Streamlit
            st.metric(
                label="MSFT Monthly Sharpe Ratio",
                value=f"{monthly_sharpe_ratio:.3f}"
            )

        else:
            st.error("Cannot calculate Sharpe Ratio.")

    else:
        st.error("Insufficient monthly data.")

else:
    st.error("No data found for MSFT.")
