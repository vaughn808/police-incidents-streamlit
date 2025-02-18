import streamlit as st
import pandas as pd

st.title("Data sources for dashboard")

st.header("Sources")
# test this code currently it is opening in the same tab instead of new tab
st.html("<a href='https://opendata.minneapolismn.gov/datasets/cityoflakes::police-incidents-2019/about' target='_blank'>Incidents 2019</a>")
st.html("<a href='https://opendata.minneapolismn.gov/datasets/cityoflakes::police-incidents-2020/about' target='_blank'>Incidents 2020</a>")
st.html("<a href='https://opendata.minneapolismn.gov/datasets/cityoflakes::police-incidents-2021/about' target='_blank'>Incidents 2021</a>")
st.html("<a href='https://opendata.minneapolismn.gov/datasets/cityoflakes::police-incidents-2022/about' target='_blank'>Incidents 2022</a>")
st.html("<a href='https://opendata.minneapolismn.gov/datasets/cityoflakes::police-incidents-2023/about' target='_blank'>Incidents 2023</a>")

st.header("Description of pages")
data = {'Page':['Neighborhood view','Page 2','Page 3'],
        'Description':['Displays the total amount of incidents in a neighborhood by year', 'page 2 description', 'page 3 description']}

page_df = pd.DataFrame(data)
st.dataframe(page_df, hide_index=True)

st.header("Complete dataset all years")
st.write(st.session_state.df)