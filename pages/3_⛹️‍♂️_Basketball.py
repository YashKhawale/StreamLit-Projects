import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("NBA Player Stats Analysis Web App")

st.markdown("""
This app performs simple web scraping of NBA player statistics.
* **Python libraries:** base64, streamlit, pandas, numpy, matplotlib, seaborn
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/)
""")

st.sidebar.header("User Input Features")
selected_year = st.sidebar.selectbox("Year", list(reversed(range(2000, 2025))))

# Web scraping of NBA player stats
@st.cache_data
def load_data(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    html = pd.read_html(url, header=0)
    df = html[0] # Load the first table
    raw = df.drop(df[df['Age'] == 'Age'].index) # Deletes repeating headers in content
    raw = raw.fillna(0) # Fill NaN values with 0
    playerstats = raw.drop(['Rk'], axis=1) # Drop unnecessary columns
    return playerstats
playerstats = load_data(selected_year)

# Sidebar - Team selection
sorted_unique_teams = sorted(playerstats[playerstats["Team"] != 0]["Team"].astype(str).unique())
st.sidebar.header("Filter by Teams")
selected_team = st.sidebar.multiselect("Team", sorted_unique_teams, sorted_unique_teams)

# Sidebar - Position selection
sorted_unique_positions = ["C", "PF", "SF", "SG", "PG"]
st.sidebar.header("Filter by Position")
selected_position = st.sidebar.multiselect("Position", sorted_unique_positions, sorted_unique_positions)

#Filtering data based on user input
df_selected_team = playerstats[(playerstats["Team"].isin(selected_team)) & 
                                (playerstats["Pos"].isin(selected_position))]

st.header("Display Player Stats of Selected Team(s)")
st.write("Data Dimension: " + str(df_selected_team.shape[0]) + " rows and " + str(df_selected_team.shape[1]) + " columns.")
st.dataframe(df_selected_team)

# Download NBA player stats as CSV
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode() # str <-> bytes conversion
    href = f'<a href="data:file/csv;base64,{b64}" download="nba_player_stats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap of player stats
if st.button("Show Intercorrelation Heatmap"):
    st.header("Intercorrelation Heatmap of Player Stats")
    df_selected_team.to_csv("output.csv", index=False)
    df = pd.read_csv("output.csv")

    corr = df.select_dtypes(include='number').corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(12, 10))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(f)