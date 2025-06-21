import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#reads the covid data file so that we can use it to make graphs
covid_data_file = pd.read_csv('cleaned_covid_data.csv')

#converts the date column into proper date format so python knows it's a date
covid_data_file['date'] = pd.to_datetime(covid_data_file['date'])

#filters the data so we only get info about Brazil and store it in a new variable
brazil_only_data = covid_data_file[covid_data_file['location'] == 'Brazil']

#this makes the background of the graphs have white lines to help us see better
sns.set_style('whitegrid')

#this makes a basic graph to show daily cases and the average of 7 days
plt.figure(figsize=(14, 8))

#this line draws a blue line for the daily new cases
sns.lineplot(x='date', y='new_cases', data=brazil_only_data, label='Daily New Cases', color='blue')

#this line draws an orange line for the 7-day average cases
sns.lineplot(x='date', y='7_day_avg_cases', data=brazil_only_data, label='7-Day Average', color='orange')

#this is the title that will show on top of the graph
plt.title('COVID-19 Daily New Cases in Brazil with 7-Day Average')

#this writes the word "Date" under the graph so we know what the x-axis means
plt.xlabel('Date')

#this writes the word "Number of Cases" on the side so we know what the y-axis means
plt.ylabel('Number of Cases')

#this shows the legend (the little box that tells us which color means what)
plt.legend()

#this rotates the dates a little so we can read them easier
plt.xticks(rotation=45)

#this makes sure the graph fits well and nothing gets cut off
plt.tight_layout()

#this shows the graph to us
plt.show()

#now we want to compare Brazil with South Africa so we filter again
brazil_and_south_africa = covid_data_file[covid_data_file['location'].isin(['Brazil', 'South Africa'])]

#this makes a cool interactive graph so we can see the comparison between Brazil and South Africa
comparison_graph = px.line(
    brazil_and_south_africa, 
    x='date', 
    y='new_cases', 
    color='location',
    title='Comparison of Daily New COVID-19 Cases: Brazil vs. South Africa',
    labels={'new_cases': 'New Cases', 'date': 'Date'}
)

#this shows us the interactive graph
comparison_graph.show()

comparison_data = covid_data[covid_data['location'].isin(['Brazil', 'South Africa'])]  # Filtering data for Brazil and South Africa
fig = px.line(comparison_data, x='date', y='new_cases', color='location',  # Creating an interactive line plot
              title='Comparison of Daily New COVID-19 Cases: Brazil vs. South Africa',  # Setting the title of the plot
              labels={'new_cases': 'New Cases', 'date': 'Date'})  # Customizing labels for the plot
fig.show()  # Displaying the interactive plot
