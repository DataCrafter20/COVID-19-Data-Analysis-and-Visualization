import streamlit as st
import pandas as pd
import plotly.express as px

#loads the covid data from the csv file so we can use it later
covid_data_from_file = pd.read_csv('covid-data-raw.csv')

#changes the 'date' column into a datetime type to work better with time-based charts
covid_data_from_file['date'] = pd.to_datetime(covid_data_from_file['date'])

#shows the title of the app at the top of the page
st.title("COVID-19 Monitoring and Analysis Dashboard")

#asks the user to pick a country from the dropdown on the sidebar
user_selected_country = st.sidebar.selectbox("Pick a Country to See Data:", covid_data_from_file['location'].unique())

#asks the user which chart type they want to see using radio buttons
user_selected_chart_type = st.sidebar.radio("Choose a Chart Type:", ["Line Chart", "Bar Chart"])

#filters the data and keeps only the rows for the country the user picked
filtered_data_by_country = covid_data_from_file[covid_data_from_file['location'] == user_selected_country]

#if the user picked "Line Chart", then show a line chart
if user_selected_chart_type == "Line Chart":
    
    #draws a line chart that shows new covid cases over time
    line_chart = px.line(
        filtered_data_by_country,
        x='date',
        y='new_cases',
        title=f'New COVID-19 Cases in {user_selected_country}'
    )

    #displays the line chart in the app
    st.plotly_chart(line_chart)

#if the user picked "Bar Chart", then show a bar chart
elif user_selected_chart_type == "Bar Chart":
    
    #draws a bar chart that shows new covid cases over time
    bar_chart = px.bar(
        filtered_data_by_country,
        x='date',
        y='new_cases',
        title=f'Daily New COVID-19 Cases in {user_selected_country}'
    )

    #displays the bar chart in the app
    st.plotly_chart(bar_chart)

#checkbox that lets the user choose if they want to see stats
if st.sidebar.checkbox("Show Stats for This Country"):
    
    #writes a small heading
    st.write("Statistics Summary:")

    #shows basic stats like mean, min, max, etc. for the country the user picked
    st.dataframe(filtered_data_by_country.describe())
