import pandas as pd  # this is a library that helps work with data tables like spreadsheets

#asks the program to read the covid data from a website instead of writing the data manually
covid_data_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
covid_table = pd.read_csv(covid_data_url)

#changes the date column so that it can be used for date calculations later
covid_table['date'] = pd.to_datetime(covid_table['date'])

#removes any extra repeated rows that might mess up the results
covid_table = covid_table.drop_duplicates()

#removes rows where the country or date is missing because they are important
covid_table = covid_table.dropna(subset=['location', 'date'])
covid_table = covid_table.dropna(subset=['total_cases'])

#some of the daily case and death numbers are missing, so we fill them in using the value from the day before
covid_table['new_cases'] = covid_table['new_cases'].ffill()
covid_table['new_deaths'] = covid_table['new_deaths'].ffill()
covid_table['new_cases_smoothed'] = covid_table['new_cases_smoothed'].ffill()
covid_table['new_deaths_smoothed'] = covid_table['new_deaths_smoothed'].ffill()

#keeps only the important columns that we need for our covid data analysis
important_columns = [
    'iso_code', 'continent', 'location', 'date',
    'total_cases', 'new_cases', 'new_cases_smoothed',
    'total_deaths', 'new_deaths', 'new_deaths_smoothed',
    'total_vaccinations', 'people_vaccinated',
    'people_fully_vaccinated', 'population'
]
covid_data = covid_table[important_columns]

#removes all the early days where each country had 0 covid cases not useful for this analysis
#this finds the first date when a country had at least 1 case and keeps everything from that day forward
cleaned_covid_data = []

grouped_data = covid_data.groupby('location')
for location in grouped_data.groups:
    country_data = grouped_data.get_group(location)
    filtered_data = country_data[country_data['total_cases'] != 0]
    if len(filtered_data) > 0:
        cleaned_covid_data.append(filtered_data.iloc[0:])
cleaned_covid_data = pd.concat(cleaned_covid_data)

import os

#saves the cleaned and improved data into a new CSV file that can be used later
covid_table.to_csv('cleaned_covid_data.csv', index=False)

#prints a message to show the cleaning is finished and also shows a quick summary of the table
print("Done cleaning the covid data:")
print(covid_table.info())

#saves the cleaned covid data to the current working directory
file_name = "cleaned_covid_data.csv"
cleaned_covid_data.to_csv(file_name, index=False)

print(f"Your file has been saved as '{file_name}' in the current folder as the python script")
