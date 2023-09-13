import polars as pl
from main import polars_descriptive_stat_min, polars_descriptive_stat_mean, polars_descriptive_stat_max

def test_descriptive_statgit_min():
    # Create a Polars DataFrame
    cars = pl.DataFrame({
        "mpg": [21.0, 21.0, 22.8, 21.4, 18.7],
        "hp": [110, 110, 93, 110, 175]
    })

    target_column = "mpg"
    min_mpg = polars_descriptive_stat_min(cars, target_column)

    # Calculate the minimum manually
    calculated_min = cars[target_column].min()
    assert min_mpg == calculated_min

def test_descriptive_stat_mean():
    # Create a Polars DataFrame
    cars = pl.DataFrame({
        "mpg": [21.0, 21.0, 22.8, 21.4, 18.7],
        "hp": [110, 110, 93, 110, 175]
    })

    target_column = "mpg"
    mean_mpg = polars_descriptive_stat_mean(cars, target_column)

    # Calculate the mean manually
    calculated_mean = cars[target_column].mean()
    assert mean_mpg == calculated_mean

def test_descriptive_stat_max():
    # Create a Polars DataFrame
    cars = pl.DataFrame({
        "mpg": [21.0, 21.0, 22.8, 21.4, 18.7],
        "hp": [110, 110, 93, 110, 175]
    })

    target_column = "mpg"
    max_mpg = polars_descriptive_stat_max(cars, target_column)

    # Calculate the maximum manually
    calculated_max = cars[target_column].max()
    assert max_mpg == calculated_max

if __name__ == "__main__":
    test_descriptive_stat_min()
    test_descriptive_stat_mean()
    test_descriptive_stat_max()