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

#some of the daily case and death numbers are missing, so we fill them in using the value from the day before
covid_table['new_cases'] = covid_table['new_cases'].fillna(method='ffill')
covid_table['new_deaths'] = covid_table['new_deaths'].fillna(method='ffill')

#removes very low or very high numbers that are probably wrong using the 1% and 99% cutoff
minimum_allowed_cases = covid_table['new_cases'].quantile(0.01)
maximum_allowed_cases = covid_table['new_cases'].quantile(0.99)

#keeps only the numbers that are between the min and max allowed limits
covid_table = covid_table[
    (covid_table['new_cases'] >= minimum_allowed_cases) &
    (covid_table['new_cases'] <= maximum_allowed_cases)
]

#adds a new column that shows the 7-day average to make trends easier to see
covid_table['average_7_day_cases'] = covid_table.groupby('location')['new_cases'].transform(
    lambda numbers: numbers.rolling(7).mean()
)

#saves the cleaned and improved data into a new CSV file that can be used later
covid_table.to_csv('data/cleaned_covid_data.csv', index=False)

#prints a message to show the cleaning is finished and also shows a quick summary of the table
print("Done cleaning the covid data:")
print(covid_table.info())
