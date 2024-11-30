## COVID-19-Data-Analysis-and-Visualization
A Python project for cleaning, analyzing, and visualizing COVID-19 data using Pandas, Matplotlib, and Streamlit. Features include data preprocessing, EDA, and an interactive dashboard to display trends and statistics. Ideal for showcasing data wrangling and visualization skills for data science.

## Project Overview
This project showcases skills in data cleaning, analysis, and visualization by exploring COVID-19 data. The dataset is sourced from [Our World in Data](https://ourworldindata.org/coronavirus) and includes information on cases, vaccinations, and deaths. The project culminates in an interactive dashboard to visualize key trends.

## Project Structure
The repository is organized as follows:

- `data/`:
  - Contains raw(compressed, extracion required) and cleaned datasets.
  - Includes intermediary processed files.
- `scripts/`:
  - Python scripts for reproducible data cleaning and visualization tasks.
  - Includes code for generating the interactive dashboard.
- `requirements.txt`:
  - Lists Python dependencies for replicating the project environment.
- `LICENSE`:
  - Project license (MIT License).
- `README.md`:
  - This file.

## Key Features
- **Data Cleaning**:
  - Filling missing values, removing duplicates, and handling outliers.
  - Adding custom columns for analysis, such as rolling averages and normalized metrics.
- **Data Visualization**:
  - Time-series plots of cases, deaths, and vaccinations.
  - Geographical maps to compare trends across countries.
  - Interactive charts for better user engagement.
- **Interactive Dashboard**:
  - Built using Streamlit to visualize data in real time.
  - Includes filters for selecting specific countries, time ranges, and metrics.

## How to Run the Project

### Prerequisites
- Python 3.8 or higher
- Recommended IDE: Jupyter Notebook or VS Code

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/covid-data-analysis.git
   ```
2. Navigate to the project folder:
   ```bash
   cd covid-data-analysis
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the interactive dashboard:
   ```bash
   streamlit run scripts/dashboard.py
   ```

## Visualizations
The project includes:
- Global and country-specific trends for COVID-19 cases and vaccinations.
- Heatmaps showing vaccination coverage across regions.
- Customizable charts for comparing metrics over time.

## Example Screenshots
_Add screenshots or GIFs showcasing your dashboard and key visualizations._

## Future Improvements
- Add more granular filters, such as age group or gender.
- Incorporate machine learning models for trend prediction.
- Enhance dashboard responsiveness for mobile devices.

## Contributing
Contributions are welcome! Please create a pull request or open an issue to discuss changes.

## License
This project is licensed under the [MIT License](LICENSE).

## Conclusion
This project demonstrates data cleaning, visualization, and interactive dashboard creation using Python.

