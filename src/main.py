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
    # Define custom colors for the scatter plot based on a column (e.g., 'cyl')
    colors = df['cyl'].apply(lambda x: x * 20)  # Adjust the scaling factor as needed
    
    # Define custom marker size based on another column (e.g., 'disp')
    marker_size = df['disp'].apply(lambda x: x / 10)  # Adjust the scaling factor as needed
    
    plt.scatter(df["mpg"], df["hp"], c=colors, cmap='viridis', s=marker_size, alpha=0.7)
    plt.xlabel("Miles Per Gallon")
    plt.ylabel("Horse Power")
    plt.title("How automobile weight changes mileage")
    plt.colorbar(label='Color')
    plt.show()

if __name__ == '__main__':
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    print(cars.head())
    print("Mean MPG:", polars_descriptive_stat_mean(cars, 'mpg'))
    print("Median MPG:", polars_descriptive_stat_median(cars, 'mpg'))
    print("Standard Deviation MPG:", polars_descriptive_stat_std(cars, 'mpg'))
    print("Max MPG:", polars_descriptive_stat_max(cars, 'mpg'))
    visualize_data(cars)