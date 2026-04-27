# Population Python Mini Project

## Introduction
This mini project studies the relationship between population growth and economic development across countries using Python.  
Using data from the World Bank Indicators API and comparing population growth rates and GDP per capita in 2024.

## Thesis
In 2024, there is a negative relationship between population growth rate and GDP per capita across countries.

## Project Organization
- `notebooks/population_project.ipynb`: contains the full exploratory analysis, charts, and conclusions
- `src/`: contains a OOP structure with Domain, Persistence, Services, and UI layers
- `src/UI/main.py`: runs a CLI-style result summary using the cleaned project data
- `output/test_run.png`: is the output evidence for my thesis

## Data Source
I uses the World Bank Indicators API.
- Population growth (annual %): SP.POP.GROW (https://data.worldbank.org/indicator/SP.POP.GROW)
- GDP per capita (current US$): NY.GDP.PCAP.CD (https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)

## Tools
- Python
- Jupyter Notebook
- pandas
- requests
- matplotlib

## How to run
### Way 1: Jupyter-notebook
- Open Anaconda Prompt
- Create and activate the project environment(conda activate population_project)
- Move to the folder(cd /d D:\github_documents\population-mini-project)
- open Jupyter-Notebook(jupyter notebook)
- Open the ipynb file(notebooks/population_project.ipynb)
- Run the cells

### run the OOP system and prints a short research-style result.
- Open Anaconda Prompt
- Run: conda activate population_project
- Run: cd /d D:\github_documents\population-mini-project\src\UI
- Run: python main.py

## Methods
- downloaded all API pages instead of using only the first page
- kept useful columns
- kept only country-level observations
- converted the year column to numeric (datatype)
- filtered the dataset to 2024 only
- merging
- removed missing values (missing value)
- checked for duplicated values (duplicated value)

## Data structures used + Big O notes
### data structures:
- Array/List: used to collect API records across pages before converting them into tables(like gdp_all_records = [], country_names = [])
- HashMap/Dictionary: used to read nested API response fields such as "item["value"]", "data[0]["pages"]"

### Big O note
- Downloading API records across all pages is approximately O(n) because each record is processed once, grouping countries and calculating average GDP per capita is approximately O(n)
- Extracting country names from API, filtering rows for the year 2024, assigning countries to quartile groups is O(n)
- Merging the population and GDP tables is approximately as O(n + m)

## Findings
### Correlation
- The correlation between population growth and GDP per capita in 2024 was: -0.12098, which suggests a weak negative relationship.
### Quartile Analysis
- Countries were divided into four quartiles based on population growth rate.
- Average GDP per capita by quartile: Q1 (lowest 25%) = 30541.75, Q2 (25%-50%) = 24372.50, Q3 (50%-75%) = 19499.17, Q4 (highest 25%) = 10835.45
- This shows that countries in the lowest population growth quartile had the highest average GDP per capita, while countries in the highest population growth quartile had the lowest average GDP per capita.
### Charts
- This project includes: "output/scatter_plot.png" and "output/quartile_bar_chart.png"
- Scatter plot of population growth vs GDP per capita in 2024.
- Bar chart of average GDP per capita by population growth quartile in 2024.

## Required features (functional checklist)
### Data ingestion
- Original population dataset with 17556 rows of population growth data and 217 after data cleaning and filtering only 2024 data
- Original gdp dataset with 17556 rows of gdp per capita data and 192 after data cleaning and filtering only 2024 data
- Final dataset after merging includes 192 rows of unique countries and 6 columns including country_name, countryiso3code, date, population_growth, region_name, gdp_per_capita

### Analysis
- computed metric：correlation
- grouping/aggregation：quartile grouping + average GDP per quartile
- “what-if” filter: data only from 2024

### Output (This project provides a short research-style result through the notebook analysis and the output in main.py)
- Thesis: In 2024, there is a negative relationship between population growth rate and GDP per capita across countries.
- Dataset Used: World Bank Indicators API
- Methods: API collection, cleaning, merging, correlation analysis, quartile grouping
- Results: Correlation = -0.12098; countries in the highest population growth quartile had the lowest average GDP per capita
- Conclusion: The thesis is supported, but weakly.


## Conclusion
- The results suggest a weak negative relationship between population growth and GDP per capita across countries in 2024.
- The correlation is negative and weak. The quartile analysis shows the same thing that countries with lower population growth tended to have higher average GDP per capita, while countries with higher population growth tended to have lower average GDP per capita.
- Overall, the thesis is supported, but weakly.
- There are some limitations like that I only used data in 2024, some countries were excluded because of missing data, and I focuses on only country-level comparison.
