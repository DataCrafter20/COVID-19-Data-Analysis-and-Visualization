import streamlit as st  # Import the Streamlit library for creating web applications
import pandas as pd  # Import the Pandas library for data manipulation and analysis
import plotly.express as px  # Import Plotly Express for creating visualizations

# Load the data
covid_data = pd.read_csv('data/cleaned_covid_data.csv')  # Read the cleaned COVID-19 data from a CSV file
covid_data['date'] = pd.to_datetime(covid_data['date'])  # Convert the 'date' column to datetime format

# Title of the dashboard
st.title("Interactive COVID-19 Data Analysis Dashboard")  # Set the title of the Streamlit app

# Sidebar for selecting country and visualization type
selected_country = st.sidebar.selectbox("Choose a Country:", covid_data['location'].unique())  # Create a dropdown to select a country
selected_chart = st.sidebar.radio("Select Chart Type:", ["Line Chart", "Bar Chart"])  # Create radio buttons to select chart type

# Filter data for the chosen country
country_data = covid_data[covid_data['location'] == selected_country]  # Filter the data for the selected country

# Plot based on user selection
if selected_chart == "Line Chart":  # Check if the selected chart type is Line Chart
    fig = px.line(country_data, x='date', y='new_cases', title=f'New COVID-19 Cases in {selected_country}')  # Create a line chart
    st.plotly_chart(fig)  # Display the line chart in the Streamlit app
elif selected_chart == "Bar Chart":  # Check if the selected chart type is Bar Chart
    fig = px.bar(country_data, x='date', y='new_cases', title=f'Daily New COVID-19 Cases in {selected_country}')  # Create a bar chart
    st.plotly_chart(fig)  # Display the bar chart in the Streamlit app

# Option to show statistics
if st.sidebar.checkbox("Show Statistics"):  # Create a checkbox to show summary statistics
    st.write("Summary Statistics:")  # Display a header for the statistics section
    st.dataframe(country_data.describe())  # Show the summary statistics of the filtered data
