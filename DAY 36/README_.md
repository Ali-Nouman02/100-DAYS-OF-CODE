# Stock Price and News Alert 🚀

This project is a Python-based automation tool that monitors stock prices and sends email alerts with news articles if the stock price changes significantly. It fetches stock price data from Alpha Vantage, retrieves relevant news articles from NewsAPI, and sends the updates via email.

## Features

1. **Stock Price Monitoring**:
   - Tracks the daily closing price of a specific stock (e.g., Tesla Inc - `TSLA`).
   - Calculates the percentage change between the last two trading days.

2. **News Fetching**:
   - If the price change exceeds 5%, fetches the top 3 news articles related to the company.

3. **Email Alerts**:
   - Sends an email for each news article, detailing the stock change, headline, and a brief description.

4. **Customizable**:
   - Easily replace the stock symbol (`STOCK_NAME`) and company name (`COMPANY_NAME`) to track other stocks.

## Setup

1. **Install Required Libraries**:
   Ensure you have Python installed along with the required libraries:
   ```bash
   pip install requests
   
2. **Get API Keys**:
   - Alpha Vantage API Key:replace YOUR_ALPHA_VANTAGE_API_KEY in the code.

3. **Configure Email Credentials**:
   Update the my_email and password variables with your email and password.
   Replace the recipient email in to_addrs with the desired recipient.
   
4. **Run the Script: Execute the script**:
     ```bash
   python main.py

## Code Workflow
1. **Stock Data Fetching**:
   Uses Alpha Vantage's TIME_SERIES_INTRADAY endpoint to fetch stock prices.
      
2. **Price Change Calculation**:
   Calculates the percentage difference between the closing prices of the last two trading days.
   If the change exceeds 5%, triggers news fetching and email alerts.
   
3. **News Articles Retrieval**:
   Fetches the top 3 news articles from NewsAPI for the specified company.
   
4. **Email Alerts**:
  Sends an email with:
  The stock ticker and percentage change (up or down).
  A headline and a brief description of each news article.







   
