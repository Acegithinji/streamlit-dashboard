import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
data = pd.read_csv('/mnt/data/dataset.csv')

# Set Streamlit page config
st.set_page_config(page_title="Employment Status in Kenya", layout="wide")

# Sidebar Filter
st.sidebar.title("Filter by Sex")
sex_filter = st.sidebar.selectbox("Select Sex", ["All", "Female", "Male"])

# Filter data by sex if selected
if sex_filter != "All":
    data = data[data['sex'] == sex_filter.lower()]

# Title
st.title("Employment Status Trends in Kenya")

# Section 1: Employment Status Trends
st.header("Employment Status Trends")
col1, col2, col3 = st.columns(3)

# Line Charts
with col1:
    fig_inactive = px.line(data, x='year', y='inactive_population', color='sex',
                           title="Total Inactive Population by Year and Sex")
    st.plotly_chart(fig_inactive, use_container_width=True)

with col2:
    fig_unemployed = px.line(data, x='year', y='unemployed_population', color='sex',
                             title="Total Unemployed Population by Year and Sex")
    st.plotly_chart(fig_unemployed, use_container_width=True)

with col3:
    fig_employed = px.line(data, x='year', y='employed_population', color='sex',
                           title="Total Employed Population by Year and Sex")
    st.plotly_chart(fig_employed, use_container_width=True)

# Pie/Donut Charts
st.header("Population Distribution by Sex")
col1, col2, col3 = st.columns(3)

with col1:
    fig_inactive_pie = px.pie(data, values='inactive_population', names='sex',
                              title="Total Inactive Population by Sex", hole=0.4)
    st.plotly_chart(fig_inactive_pie, use_container_width=True)

with col2:
    fig_unemployed_pie = px.pie(data, values='unemployed_population', names='sex',
                                title="Total Unemployed Population by Sex", hole=0.4)
    st.plotly_chart(fig_unemployed_pie, use_container_width=True)

with col3:
    fig_employed_pie = px.pie(data, values='employed_population', names='sex',
                              title="Total Employed Population by Sex", hole=0.4)
    st.plotly_chart(fig_employed_pie, use_container_width=True)

# Section 2: Employment Status by Education Level
st.header("Employment Status by Education Level in Kenya")

# Tabs for each education level
education_levels = ['Basic', 'Intermediate', 'Advanced']
for level in education_levels:
    with st.expander(f"{level} Education"):
        col1, col2 = st.columns(2)

        # Donut Chart for Inactive Population by Sex
        with col1:
            fig_inactive_edu = px.pie(data[data['education_level'] == level.lower()],
                                      values='inactive_population', names='sex',
                                      title=f"{level} Education - Inactive Population by Sex", hole=0.5)
            st.plotly_chart(fig_inactive_edu, use_container_width=True)

        # Bar Chart for Unemployed by Age Group and Sex
        with col2:
            fig_unemployed_age = px.bar(data[data['education_level'] == level.lower()],
                                        x='age_group', y='unemployed_population', color='sex',
                                        title=f"{level} Ed - Unemployed by Age Group and Sex")
            st.plotly_chart(fig_unemployed_age, use_container_width=True)
