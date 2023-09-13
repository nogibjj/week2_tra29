import polars as pl
import matplotlib.pyplot as plt

def polars_descriptive_stat_mean(df: pl.DataFrame, col: str) -> float:
    return df[col].mean()

def polars_descriptive_stat_median(df: pl.DataFrame, col: str) -> float:
    return df[col].median()

def polars_descriptive_stat_std(df: pl.DataFrame, col: str) -> float:
    return df[col].std()

def polars_descriptive_stat_max(df: pl.DataFrame, col: str) -> float:
    return df[col].max()

def visualize_data(df):
    plt.scatter(df["mpg"], df["hp"])
    plt.xlabel("Miles Per Gallon")
    plt.ylabel("Horse Power")
    plt.title("How automobile weight changes mileage")
    plt.show()

if __name__ == '__main__':
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    print(cars.head())
    print("Mean MPG:", polars_descriptive_stat_mean(cars, 'mpg'))
    print("Median MPG:", polars_descriptive_stat_median(cars, 'mpg'))
    print("Standard Deviation MPG:", polars_descriptive_stat_std(cars, 'mpg'))
    print("Max MPG:", polars_descriptive_stat_max(cars, 'mpg'))
    visualize_data(cars)