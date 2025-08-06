# 📊 Streamlit Projects by Yash Khawale

Welcome to **Yash Khawale's Streamlit Projects** repository!

This is a multi-page Streamlit web application demonstrating various data-driven mini-projects including stock visualization, sports analytics, and financial data exploration.

---

## 🗂️ Projects Included

### 🏠 1. Homepage
- A welcoming dashboard for the web app
- Summary of available projects
- Quick navigation via sidebar

---

### 📈 2. Apple Stock Price Graph
**File:** `2_📈_Stock_Graph.py`  
- Displays **Apple Inc. (AAPL)** stock data from 2010 to 2020
- Shows **closing price** and **volume**
- Visualization: Streamlit line charts

---

### ⛹️‍♂️ 3. NBA Player Stats Analyzer
**File:** `3_⛹️‍♂️_Basketball.py`  
- Web scraping of NBA per-game stats from [Basketball Reference](https://www.basketball-reference.com/)
- Filter players by **year**, **team**, and **position**
- Download data as CSV file
- Generate **intercorrelation heatmap** for stats

---

### ⚽ 4. NFL Rushing Stats Analyzer
**File:** `4_⚽_Football.py`  
- Scrapes NFL player rushing data from [Pro Football Reference](https://www.pro-football-reference.com/)
- Filter by **year**, **team**, and **position**
- Download data as CSV file
- Generate heatmap for statistical correlation

---

### 📃 5. S&P 500 Stock Explorer
**File:** `5_📃_SP500_Stock_List.py`  
- Scrapes list of S&P 500 companies from [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
- Filter companies by **sector** and **headquarter location**
- Plots **YTD stock prices** of selected companies using `yfinance`
- Customize number of companies to plot
- CSV download supported

---

## ⚙️ Tech Stack

- **Framework:** Streamlit
- **Languages:** Python
- **Libraries:** `pandas`, `yfinance`, `matplotlib`, `seaborn`, `numpy`, `base64`
- **Data Sources:** Wikipedia, Yahoo Finance, Basketball Reference, Pro Football Reference

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YashKhawale/StreamLit-Projects.git
   cd StreamLit-Projects
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run 1_🏠_Homepage.py
   ```

4. Use the **sidebar** to explore different project pages.

---

## 📂 File Structure

```
├── 1_🏠_Homepage.py              # Main homepage
├── 2_📈_Stock_Graph.py           # Apple stock graph
├── 3_⛹️‍♂️_Basketball.py         # NBA player stats
├── 4_⚽_Football.py              # NFL rushing stats
├── 5_📃_SP500_Stock_List.py      # S&P 500 company and stock analysis
```

---

## ✍️ Author

**Yash Khawale**  
Made with ❤️ using Python and Streamlit.
