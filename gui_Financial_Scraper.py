import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Financial Stock Analyzer", layout="wide", initial_sidebar_state="expanded")      # Set page configuration. it sets the title (What appears as the tab name), the layout of the contents and how we want the sidebar to behave once we initially launch the app.

#Working on the Sidebar#
st.sidebar.title("Stock Analyzer")                                                                                                            
ticker=st.sidebar.text_input('Enter stock ticker',value='AAPL',help='Example: AAPL, MSFT, TSLA').upper()        # Get user input for stock ticker symbol. Default is 'AAPL'. The input is converted to uppercase to match standard ticker formats.           


period=st.sidebar.selectbox('Select period for analysis',('1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'),index=3)       # Allow user to select the time period for analysis from predefined options. Default is '1y'.


#Working on the Main Page Content#
st.title(f"{ticker} Stock Analysis")        # Set the main title of the app dynamically based on the ticker symbol.


#Downloading Stock Data#
def load_data(ticker, period):      # Function to load historical stock data using yfinance library.
    data=yf.Ticker(ticker).history(period=period)
    return data 

data=load_data(ticker, period)


#Error Handling for invalid ticker symbols#
if data.empty:          # Check if the data is empty. This is incase an invalid ticker symbol is entered (Error Handling). Incase 'True', it prints 'invalid ticker or no data available'.
    st.error('Error: No such data exists or Invalid Ticker')
    st.stop()


#Data Analysis#
data['Daily Return']= data['Close'].pct_change()                     #Adj Close used instead of Close to account for dividends and stock splits.
average_daily_return=data['Daily Return'].mean()*252
volatility= data['Daily Return'].std() * (252**0.5)
annualized_return=(1+data['Daily Return']).prod()**(252/len(data))-1


data['MA50'] = data['Close'].rolling(50).mean()
data['MA200'] = data['Close'].rolling(200).mean()


data['Signal']=0
data.loc[data['MA50'] > data['MA200'], 'Signal']=1
data['Position']=data['Signal'].diff()

latest_price=data['Close'].iloc[-1]

#Data Visualization#
col1, col2, col3, col4 = st.columns(4)                  # Create four columns to display key metrics side by side.

col1.metric("Latest Price", f"${latest_price:.2f}")
col2.metric("Annualized Mean Return", f"{average_daily_return*100:.2f}%")
col3.metric("Compounded Annualized Return", f"{annualized_return*100:.2f}%")
col4.metric("Annualized Volatility", f"{volatility*100:.2f}%")


#Graphical Visualization#
fig,ax=plt.subplots(figsize=(12,6))

fig.patch.set_facecolor('#212121')
ax.set_facecolor('#15181C')

ax.plot(data['Close'], label='Close Price', color='gray')
ax.plot(data['MA50'], label= '50 day MA', color='purple', alpha=0.9)
ax.plot(data['MA200'], label='200 day MA', color='lightblue', alpha=0.9)
ax.plot(data[data['Position']==1].index,data['MA50'][data['Position']==1],'^',markersize=5,color='g',label='Buy Signal' )
ax.plot(data[data['Position']==-1].index,data['MA50'][data['Position']==-1],'v', markersize=5, color='r', label='Sell Signal')

ax.set_title(f'{ticker} Price Chart with Moving Averages', color='white')
ax.set_xlabel('Date', color='white')
ax.set_ylabel('Price ($)', color='white')

ax.tick_params(colors='white')
ax.grid(True, color='#2a2e33',alpha=0.4)

ax.legend(facecolor='#15181C', edgecolor='white', labelcolor='white')

st.pyplot(fig)


#Displaying Raw Data#
with st.expander('View Raw Data'):      # Done with the help of an expander so as to maintain clean interface, yet giving the user the option to view the raw DataFrame that we used to perform the analysis. 
    st.dataframe(data.style.format({'Close':'${:,.2f}','Daily Return':'{:.4%}','MA50':'${:,.2f}','MA200':'${:,.2f}'}),height=400)



