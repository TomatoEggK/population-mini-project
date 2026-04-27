import pandas as pd

class Cleaner: # data cleaning including deleting unuseful columns, keeping real country data, renaming columns, removing missing values and duplicated values
    def clean_indicator_data(self, df, value_name, year):
        df = df[["country", "countryiso3code", "date", "value"]].copy()  # Keep useful columns

        country_names = []  # Store extracted country names
        for item in df["country"]:
            country_names.append(item["value"])  # add them

        df["country_name"] = country_names  # Save country names
        df["date"] = pd.to_numeric(df["date"], errors="coerce")  # Convert year to numeric

        df = df[df["date"] == year].copy()  # Keep only the selected year(We will choose 2024)
        df = df.rename(columns={"value": value_name})  # Rename column
        df = df.dropna(subset=[value_name])  # Remove missing values

        return df

    def clean_country_metadata(self, df):
        df = df[["id", "name", "region"]].copy()  # Keep useful columns

        region_names = []
        for item in df["region"]:
            region_names.append(item["value"])

        df["region_name"] = region_names
        df = df.rename(columns={"id": "countryiso3code", "name": "meta_country_name"})  # Rename columns
        df = df[df["region_name"] != "Aggregates"].copy()  # Keep only countries

        return df

    def merge_final_data(self, pop_df, gdp_df, country_df):
        pop_country = pd.merge(
            pop_df,
            country_df[["countryiso3code", "region_name"]],
            on="countryiso3code",
            how="inner"
        )  # Keep only real countries in population data

        gdp_country = pd.merge(
            gdp_df,
            country_df[["countryiso3code", "region_name"]],
            on="countryiso3code",
            how="inner"
        )  # Keep only real countries in GDP data

        final_df = pd.merge(
            pop_country[["country_name", "countryiso3code", "date", "population_growth", "region_name"]],
            gdp_country[["countryiso3code", "gdp_per_capita"]],
            on="countryiso3code",
            how="inner"
        )  # Merge

        final_df = final_df.drop_duplicates()  # duplicate rows
        return final_df