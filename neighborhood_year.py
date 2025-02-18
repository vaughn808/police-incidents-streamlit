import streamlit as st
import pandas as pd

st.title("Minneapolis Police Incidents by Year and Neighborhood")

left,mid_left, mid_middle,right = st.columns([.2,.2,.2,.4], vertical_alignment="center")

sel_neigh = left.selectbox(
    "Neighborhood",
    st.session_state.neighborhood_df,
    index=None,
    placeholder="Please select the Neighborhood",
)

sel_year = mid_left.selectbox(
    "Year",
    st.session_state.year_df,
    index=None,
    placeholder="Please select the year",
)

if sel_year != None and sel_neigh != None:
    #data = st.session_state.df.query(f'report_year == {str(sel_year)}') 
    data = st.session_state.df.query(f'neighborhood == "{sel_neigh}" and report_year =="{sel_year}"')
    
    sel_desc = mid_middle.selectbox(
    "Description",
    data.description.unique(),
    index=None,
    placeholder="Please select crime description",
    )

    #area_df = data['description'].value_counts().rename('description')
    data['Counts'] = data.groupby(['description'])['description'].transform('count')
    dff = data.filter(['description', 'Counts']).drop_duplicates().reset_index(drop=True)
    #dff = dff.drop_duplicates().reset_index(drop=True)
    
    st.write(dff)
    st.area_chart(dff, x="description", y="Counts", color="description", stack="center")
    st.bar_chart(dff, x="description", y="Counts")
    if sel_desc != None:
        data = st.session_state.df.query(f'neighborhood == "{sel_neigh}" and report_year =="{sel_year}" and description =="{sel_desc}"')
        st.write(data)
        st.map(data, latitude="centerLat", longitude="centerLong", size = 2)
