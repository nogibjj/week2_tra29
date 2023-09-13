import polars as pl

def test_descriptive_stat_mean():
    # Import the DataFrame from the CSV file
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")

    target_column = "mpg"
    expected_mean = cars[target_column].mean()

    # Calculate the mean using the function
    calculated_stats = descriptive_stat_mean(cars, target_column)

    # Extract the mean from the summary statistics
    calculated_mean = calculated_stats[target_column].filter(pl.col("summary") == "mean").select(target_column).to_pandas().iloc[0, 0]

    # Use assert to compare the calculated mean with the expected mean
    assert calculated_mean == expected_mean

if __name__ == "__main__":
    test_descriptive_stat_mean()
