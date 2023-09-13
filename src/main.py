import polars as pl
import matplotlib.pyplot as plt

def polars_descriptive_stat_min(df: pl.DataFrame, col: str) -> float:
    return df[col].min()  # Calculate the minimum value

def polars_descriptive_stat_mean(df: pl.DataFrame, col: str) -> float:
    return df[col].mean()  # Calculate the mean value

def polars_descriptive_stat_max(df: pl.DataFrame, col: str) -> float:
    return df[col].max()  # Calculate the maximum value

def visualize_data(df):
    plt.scatter(df["mpg"], df["hp"])
    plt.xlabel("Miles Per Gallon")
    plt.ylabel("Horse Power")
    plt.title("Miles per gallon changes with automobile weight")
    plt.show()

if __name__ == '__main__':
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    print(cars.head())
    
    # Calculate and print the minimum, mean, and maximum values
    print("Minimum:", polars_descriptive_stat_min(cars, 'mpg'))
    print("Mean:", polars)
