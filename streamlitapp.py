import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Combined Employment Status in Kenya", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv('dataset.csv')

data = load_data()


# Sidebar Filters for sex and age group
#Sex
st.sidebar.title("Filter by Sex")
sex_filter = st.sidebar.selectbox("Select Sex", ["All", "Female", "Male"])
if sex_filter != "All":
    data = data[data['sex'] == sex_filter.lower()]
    
#Age group
st.sidebar.title("Filter by Age Group")
age_group_filter = st.sidebar.selectbox("Select Age Group", ["All", "15-24", "25-35"])
if age_group_filter != "All":
    data = data[data['age_group'] == age_group_filter.lower()]
    
    

#Visuals for population trends over the years
age_groups = data['age_group'].unique()
selected_age_group = st.sidebar.selectbox("Select Age Group for population trends visual", age_groups)
filtered_data = data[data['age_group'] == selected_age_group]
annual_data = filtered_data.groupby('year').agg({
    'total_inactive_population': 'sum',
    'total_unemployed_population': 'sum',
    'total_employed_population': 'sum'
}).reset_index()
st.title("Population Distribution Trends in Kenya")

# Section header for Population Trends by Employment Status
st.header("Population Trends Over the Years")
st.subheader(f"Displaying aggregated data for Age Group: {selected_age_group}")

col1, col2, col3 = st.columns(3)

# Line Chart for Total Inactive Population
with col1:
    fig_inactive = px.line(
        annual_data, x='year', y='total_inactive_population',
        title="Inactive Population Over the Years",
        labels={"total_inactive_population": "Inactive Population", "year": "Year"}
    )
    fig_inactive.update_traces(mode="lines+markers")
    st.plotly_chart(fig_inactive, use_container_width=True)

# Line Chart for Total Unemployed Population
with col2:
    fig_unemployed = px.line(
        annual_data, x='year', y='total_unemployed_population',
        title="Unemployed Population Over the Years",
        labels={"total_unemployed_population": "Unemployed Population", "year": "Year"}
    )
    fig_unemployed.update_traces(mode="lines+markers")
    st.plotly_chart(fig_unemployed, use_container_width=True)

# Line Chart for Total Employed Population
with col3:
    fig_employed = px.line(
        annual_data, x='year', y='total_employed_population',
        title="Employed Population Over the Years",
        labels={"total_employed_population": "Employed Population", "year": "Year"}
    )
    fig_employed.update_traces(mode="lines+markers")
    st.plotly_chart(fig_employed, use_container_width=True)

#Visuals for population distribution by sex
st.header("Population Distribution by Sex")
col1, col2, col3 = st.columns(3)

#Pie charts for population distribution by sex
with col1:
    fig_inactive_pie = px.pie(data, values='total_inactive_population', names='sex',
                              title="Total Inactive Population by Sex", hole=0.4)
    st.plotly_chart(fig_inactive_pie, use_container_width=True)

with col2:
    fig_unemployed_pie = px.pie(data, values='total_unemployed_population', names='sex',
                                title="Total Unemployed Population by Sex", hole=0.4)
    st.plotly_chart(fig_unemployed_pie, use_container_width=True)

with col3:
    fig_employed_pie = px.pie(data, values='total_employed_population', names='sex',
                              title="Total Employed Population by Sex", hole=0.4)
    st.plotly_chart(fig_employed_pie, use_container_width=True)
    
#Visuals for population distribution by age group
st.header("Population Distribution by Age Group")
col1, col2, col3 = st.columns(3)

#Pie charts for population distribution by age group
with col1:
    fig_inactive_pie = px.pie(data, values='total_inactive_population', names='age_group',
                              title="Total Inactive Population by Age Group", hole=0.4)
    st.plotly_chart(fig_inactive_pie, use_container_width=True)

with col2:
    fig_unemployed_pie = px.pie(data, values='total_unemployed_population', names='age_group',
                                title="Total Unemployed Population by Age Group", hole=0.4)
    st.plotly_chart(fig_unemployed_pie, use_container_width=True)

with col3:
    fig_employed_pie = px.pie(data, values='total_employed_population', names='age_group',
                              title="Total Employed Population by Age Group", hole=0.4)
    st.plotly_chart(fig_employed_pie, use_container_width=True)
    


