import pandas as pd  # Import the pandas library for data manipulation

# Load the COVID-19 data from the source
covid_data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')  # Read the CSV file from the URL

# Convert 'date' column to datetime format for easier manipulation
covid_data['date'] = pd.to_datetime(covid_data['date'])  # Change the 'date' column to datetime objects

# Drop duplicate rows
covid_data = covid_data.drop_duplicates()  # Remove any duplicate entries in the DataFrame

# Drop rows where 'location' or 'date' is missing
covid_data = covid_data.dropna(subset=['location', 'date'])  # Eliminate rows with missing 'location' or 'date' values

# Fill missing values in 'new_cases' and 'new_deaths' columns using forward fill
covid_data['new_cases'] = covid_data['new_cases'].fillna(method='ffill')  # Forward fill missing 'new_cases' values
covid_data['new_deaths'] = covid_data['new_deaths'].fillna(method='ffill')  # Forward fill missing 'new_deaths' values

# Remove outliers by applying a threshold based on quantiles
lower_bound = covid_data['new_cases'].quantile(0.01)  # Calculate the 1st percentile for 'new_cases'
upper_bound = covid_data['new_cases'].quantile(0.99)  # Calculate the 99th percentile for 'new_cases'
covid_data = covid_data[(covid_data['new_cases'] >= lower_bound) & (covid_data['new_cases'] <= upper_bound)]  # Filter out outliers

# Create a new column for the rolling 7-day average of new cases
covid_data['7_day_avg_cases'] = covid_data.groupby('location')['new_cases'].transform(lambda x: x.rolling(7).mean())  # Calculate the 7-day rolling average of 'new_cases'

# Save the cleaned data to a CSV file
covid_data.to_csv('data/cleaned_covid_data.csv', index=False)  # Write the cleaned DataFrame to a CSV file without the index

# Print data summary to verify the changes
print("Data Cleaning Completed:")  # Print a completion message
print(covid_data.info())  # Display a summary of the cleaned DataFrame
