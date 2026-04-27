from Domain.models import AnalysisResult  # Import the result class


class Analyzer: # do the analyzing job
    def assign_quartile(self, value, q1, q2, q3):
        if value <= q1:
            return "Q1 (lowest 25%)"  # Lowest quarter
        elif value <= q2:
            return "Q2 (25%-50%)"  # Second quarter
        elif value <= q3:
            return "Q3 (50%-75%)"  # Third quarter
        else:
            return "Q4 (highest 25%)"  # Highest quarter

    def analyze(self, df, year):
        correlation = df["population_growth"].corr(df["gdp_per_capita"])  # Calculate correlation

        q1 = df["population_growth"].quantile(0.25)
        q2 = df["population_growth"].quantile(0.50)
        q3 = df["population_growth"].quantile(0.75)

        quartile_labels = []
        for value in df["population_growth"]:
            quartile_labels.append(self.assign_quartile(value, q1, q2, q3))  # Assign group

        df = df.copy()
        df["growth_quartile"] = quartile_labels

        quartile_gdp = df.groupby("growth_quartile")["gdp_per_capita"].mean()  # Calculate average GDP by quartile

        conclusion = "The thesis is supported."  # Default conclusion
        if correlation >= 0:
            conclusion = "The thesis is not supported."  # Update conclusion if correlation is positive

        return AnalysisResult(
            year=year,
            record_count=len(df),
            correlation=correlation,
            q1_avg_gdp=quartile_gdp.get("Q1 (lowest 25%)", 0.0),
            q2_avg_gdp=quartile_gdp.get("Q2 (25%-50%)", 0.0),
            q3_avg_gdp=quartile_gdp.get("Q3 (50%-75%)", 0.0),
            q4_avg_gdp=quartile_gdp.get("Q4 (highest 25%)", 0.0),
            conclusion=conclusion
        )