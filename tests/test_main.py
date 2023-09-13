from src.main import descriptive_stat_mean
import polars as pl

def test_descriptive_stat_mean():
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    mean_mpg = descriptive_stat_mean(cars, target_column)

    calculated_mean = cars[target_column].sum()/len(cars[target_column])
    assert mean_mpg == calculated_mean

if __name__ == "__main__":
    test_descriptive_stat_mean()
