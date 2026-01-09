# Financial_Scraper_GUI
<pre>
A Python-based interactive quantitative stock analysis dashboard built with Streamlit. 
This tool allows users to fetch historical stock data, compute key financial metrics, 
implement technical trading strategies, generate buy/sell signals, and visualize market 
behavior—all in a clean, interactive interface.

Features:
  Historical Market Data
  Fetches stock data from Yahoo Finance (yfinance) for any valid ticker symbol.
  Supports multiple time periods (1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, YTD, max).

  Quantitative Metrics:
    Daily returns and annualized volatility
    Average and compounded annualized returns
    Latest stock price

  Technical Analysis:
    50-day and 200-day moving averages
    Moving-average crossover strategy for buy/sell signal generation
    Dynamic detection and plotting of buy/sell signals

  Interactive Visualizations:
    Price charts with moving averages and annotated trade signals
    Custom dark-themed plots for better readability

  Data Exploration:
    Raw data is available in an expandable table with formatted financial metrics
    Users can inspect daily returns, moving averages, and closing prices

Technologies Used:
  Python
  Streamlit
  Pandas
  YFinance
  Matplotlib

Improvements Over Basic Analyzer:
  Fully interactive Streamlit interface for real-time analysis
  Consolidated metrics, visualization, and raw data in a single dashboard
  Robust error handling and input validation
  Enhanced user experience for both quantitative and technical analysis
</pre>
