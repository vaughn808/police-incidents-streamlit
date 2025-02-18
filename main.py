import streamlit as st
import pandas as pd
import datetime as dt

pd_data = './data/police_incidents_all_years.csv'
home = st.Page("home.py", title="Home", icon=":material/home:")
neigh_year = st.Page("neighborhood_year.py", title="Neighborhood View", icon=":material/dashboard:")

pg_list = [home, neigh_year]

pg = st.navigation(pg_list)

st.set_page_config(layout="wide")

@st.cache_data
def load_df(path):
    # Loads dataframes from csv
    data = pd.read_csv(path)

    # add the year column to dataset
    data['reportedDate'] = pd.to_datetime(data['reportedDate'],utc=True, format='mixed')
    data['report_year'] = data['reportedDate'].dt.strftime('%Y')

    data = data.dropna(subset=['X', 'Y'])

    return data

if "df" not in st.session_state:
    # Make dataframe available on other pages by putting it is tab session
    st.session_state.df = load_df(pd_data)

if "year_df" not in st.session_state:
    # Make dataframe available on other pages by putting it is tab session unique list of years
    st.session_state.year_df = ["2019", "2020", "2021", "2022", "2023"]

if "neighborhood_df" not in st.session_state:
    # Make dataframe available on other pages by putting it is tab session unique list of neighborhood
    df = st.session_state.df

    # remove rows sthat don't have data in 
    clean_df = df.dropna(subset=['X', 'Y'])

    # get unique list of neighborhoods used
    st.session_state.neighborhood_df = clean_df.neighborhood.unique()

if "desc_df" not in st.session_state:
    st.session_state.desc_df = clean_df.description.unique()

pg.run()