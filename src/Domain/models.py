from dataclasses import dataclass


@dataclass
class Record: # One record of data
    country_name: str 
    countryiso3code: str  # the country code
    date: int 
    population_growth: float | None = None  # Store the value population growth
    gdp_per_capita: float | None = None  # Store the value GDP per capita
    region_name: str | None = None 


@dataclass
class Thesis: # Research problem
    statement: str
    year: int
    variable_x: str
    variable_y: str


@dataclass
class AnalysisResult: # Result
    year: int
    record_count: int
    correlation: float
    q1_avg_gdp: float
    q2_avg_gdp: float
    q3_avg_gdp: float
    q4_avg_gdp: float
    conclusion: str