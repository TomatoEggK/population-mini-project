import sys  # Used to adjust Python import paths
import os  # Used to work with file paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # Add the src folder to the Python path

from Domain.models import Thesis 
from Persistence.api_client import ApiClient
from Persistence.repository import Repository
from Services.cleaner import Cleaner
from Services.analyzer import Analyzer


def main():
    thesis = Thesis(
        statement="In 2024, there is a negative relationship between population growth rate and GDP per capita across countries.",
        year=2024,
        variable_x="population_growth",
        variable_y="gdp_per_capita"
    )  # Create the thesis object

    api_client = ApiClient()
    cleaner = Cleaner()
    analyzer = Analyzer()
    repository = Repository()  # Create API client, cleaner, analyzer, and repository

    print("Downloading population growth data...")  # Show progress
    pop_raw = api_client.fetch_indicator("SP.POP.GROW")  # Fetch population growth data

    print("Downloading GDP per capita data...")
    gdp_raw = api_client.fetch_indicator("NY.GDP.PCAP.CD")  # Fetch GDP data

    print("Downloading country metadata...")
    country_raw = api_client.fetch_country_metadata()  # Fetch metadata

    pop_clean = cleaner.clean_indicator_data(pop_raw, "population_growth", thesis.year)
    gdp_clean = cleaner.clean_indicator_data(gdp_raw, "gdp_per_capita", thesis.year)
    country_clean = cleaner.clean_country_metadata(country_raw)   # Clean population, gdp data, and metadata

    final_df = cleaner.merge_final_data(pop_clean, gdp_clean, country_clean)
    repository.save(final_df)  # Save final dataset locally

    result = analyzer.analyze(final_df, thesis.year)  # Run the analysis

    print("\n--- Research-Style Result ---")  # title
    print("Thesis:", thesis.statement)  # thesis
    print("Dataset used: World Bank Indicators API")  # dataset source
    print("Methods: cleaning, merge, correlation, quartile grouping")  #  methods
    print("Results:")
    print("  Record count:", result.record_count)  # number of rows
    print("  Correlation:", round(result.correlation, 5))  # correlation
    print("  Q1 average GDP per capita:", round(result.q1_avg_gdp, 2))
    print("  Q2 average GDP per capita:", round(result.q2_avg_gdp, 2))
    print("  Q3 average GDP per capita:", round(result.q3_avg_gdp, 2))
    print("  Q4 average GDP per capita:", round(result.q4_avg_gdp, 2))
    print("Conclusion:", result.conclusion)  # conclusion


if __name__ == "__main__":
    main()