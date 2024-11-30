import pandas as pd  # Importing the pandas library for data manipulation and analysis
import matplotlib.pyplot as plt  # Importing matplotlib for creating static, animated, and interactive visualizations
import seaborn as sns  # Importing seaborn for statistical data visualization
import plotly.express as px  # Importing plotly express for creating interactive plots

# Load the cleaned data
covid_data = pd.read_csv('data/cleaned_covid_data.csv')  # Reading the cleaned COVID-19 data from a CSV file
covid_data['date'] = pd.to_datetime(covid_data['date'])  # Converting the 'date' column to datetime format

# Filter data for a specific country (e.g., Brazil)
brazil_data = covid_data[covid_data['location'] == 'Brazil']  # Filtering the data for Brazil

# Set up a plot style for aesthetics
sns.set_style('whitegrid')  # Setting the style of seaborn plots to 'whitegrid'

# Custom line plot showing daily new cases with the rolling average overlay
plt.figure(figsize=(14, 8))  # Creating a new figure with a specified size
sns.lineplot(x='date', y='new_cases', data=brazil_data, label='Daily New Cases', color='blue')  # Plotting daily new cases
sns.lineplot(x='date', y='7_day_avg_cases', data=brazil_data, label='7-Day Average', color='orange')  # Plotting the 7-day average cases
plt.title('COVID-19 Daily New Cases in Brazil with 7-Day Average')  # Setting the title of the plot
plt.xlabel('Date')  # Labeling the x-axis
plt.ylabel('Number of Cases')  # Labeling the y-axis
plt.legend()  # Displaying the legend
plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
plt.tight_layout()  # Adjusting the layout to prevent clipping of tick-labels
plt.show()  # Displaying the plot

# Interactive plot for a country comparison (e.g., Brazil vs. South Africa)
comparison_data = covid_data[covid_data['location'].isin(['Brazil', 'South Africa'])]  # Filtering data for Brazil and South Africa
fig = px.line(comparison_data, x='date', y='new_cases', color='location',  # Creating an interactive line plot
              title='Comparison of Daily New COVID-19 Cases: Brazil vs. South Africa',  # Setting the title of the plot
              labels={'new_cases': 'New Cases', 'date': 'Date'})  # Customizing labels for the plot
fig.show()  # Displaying the interactive plot
