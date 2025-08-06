import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import yfinance as yf

st.set_page_config(page_title="S&P 500 Stock Analysis Web App", layout="wide")

st.title("S&P 500 Stock Analysis")

st.markdown("""
This app retrieves the list of the **S&P 500** (from Wikipedia) and its corresponding **stock closing price** (year-to-date)!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header("User Input Features")

# Web scraping of S&P 500 companies
@st.cache_data
def load_data():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html = pd.read_html(url, header=0)
    df = html[0] # Load the first table
    raw = df.fillna(0)
    return raw
sp500_data = load_data()

sector = sp500_data.groupby("GICS Sector")

# Sidebar - Sector selection
sorted_unique_sectors = sorted(sp500_data["GICS Sector"].unique())
sorted_sectors = st.sidebar.multiselect("Sector", sorted_unique_sectors, sorted_unique_sectors)

# Sidebar - Country selection
locations = sp500_data["Headquarters Location"][sp500_data["Headquarters Location"] != 0].dropna().astype(str)
countries = locations.str.split(",").str[-1].str.strip()
sorted_unique_countries = sorted(countries.unique())
sorted_countries = st.sidebar.multiselect("Country", sorted_unique_countries, ["New York", "California", "Illinois", "Massachusetts", "Texas", "New Jersey", "Minnesota", "Virginia", "Connecticut", "Georgia"])

# Filtering data based on user input
df_selected_sector = sp500_data[(sp500_data["GICS Sector"].isin(sorted_sectors)) &
                                (sp500_data["Headquarters Location"].str.split(",").str[-1].str.strip().isin(sorted_countries))]

st.header("Display S&P 500 Companies of Selected Sector(s)")
st.write("Data Dimension: " + str(df_selected_sector.shape[0]) + " rows and " + str(df_selected_sector.shape[1]) + " columns.")
st.dataframe(df_selected_sector)

# Download S&P500 data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# https://pypi.org/project/yfinance/

data = yf.download(
        tickers = list(df_selected_sector[:7].Symbol),
        period = "ytd",
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )

# Plot closing price of Query Symbols
st.subheader("Closing Price of Selected Stocks")
def price_plot(symbol):
    df = pd.DataFrame(data[symbol]['Close'])
    df["Date"] = df.index
    plt.fill_between(df["Date"], df["Close"], color='skyblue', alpha=0.4)
    plt.plot(df["Date"], df["Close"], color='Slateblue', alpha=0.6, linewidth=2)
    plt.xticks(rotation=45)
    plt.title(f"Closing Price of {symbol} Stock", fontweight='bold')
    plt.xlabel("Date", fontweight='bold')
    plt.ylabel("Closing Price (USD)", fontweight='bold')
    st.pyplot(plt)

num_company = st.sidebar.slider("Number of Companies to Plot", 1, 5, 2)

if st.button("Show Plots"):
    st.header("Stock Closing Price Plots")
    for symbol in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(symbol)