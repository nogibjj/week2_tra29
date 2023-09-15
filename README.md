# IDS706-python-template [![CI](https://github.com/nogibjj/week3_tra29/actions/workflows/python_ci_cd.yml/badge.svg)](https://github.com/nogibjj/week3_tra29/actions/workflows/python_ci_cd.yml)
### by Titus Robin

# Project Title: Analyzing Car Data with Polars

## Purpose

The purpose of this project is to utilize the Polars library to load a DataFrame, specifically a `pl.DataFrame`, and perform various data analysis tasks. We aim to extract descriptive statistics from the dataset, visualize the data on a scatter plot, and automate these processes for seamless collaboration among team members.

## Dataset

The dataset used in this project consists of information about various car models, including attributes such as:

- Miles per gallon (mpg)
- Number of cylinders (cylinders)
- Gear type (gear)
- And more...

## Functions

We have implemented several functions to extract key statistics from the Polars DataFrame. These functions include:

1. `polars_descriptive_stat_mean`: Calculates the mean value of a specified column.
2. `polars_descriptive_stat_median`: Computes the median value of a specified column.
3. `polars_descriptive_stat_std`: Determines the standard deviation of a specified column.
4. `polars_descriptive_stat_max`: Calculates the maximum value of a specified column.

Additionally, a test file has been provided to validate the accuracy of these descriptive statistics.

## Visualization

To gain insights from the dataset, we have created a scatter plot that visually compares the variables "Miles per Gallon" and "Horsepower." This visualization helps us understand the relationship between these attributes.
<img width="615" alt="Screen Shot 2023-09-13 at 4 38 39 PM" src="https://github.com/nogibjj/week3_tra29/assets/143838819/87b09499-bde8-4413-ace2-51ba72d7b623">

## Automation

To streamline the development and collaboration process, we have implemented automation tools and practices:

1. **Devcontainer**: A `.devcontainer` folder is included, which contains two important files: `Dockerfile` and `devcontainer.json`. These files define the development environment settings to ensure consistency among collaborators.

2. **Makefile**: The `Makefile` provides a set of commands for various tasks, including:

   - Installing required packages (specified in `requirements.txt`).
   - Code formatting using the `black` formatter.
   - Running tests for functions (file names starting with "Check...").
   - Code linting with `pylint`.

3. **GitHub Actions**: The project utilizes GitHub Actions, specifically the `main.yml` file, to automate tasks triggered by events like pushes or pull requests. It enforces code formatting, linting, and testing to maintain code quality.

4. **Requirements.txt**: The `requirements.txt` file lists the required Python packages for the project. While it currently contains generic Python packages, it can be extended with more specific dependencies as needed for future project scopes.

This project aims to provide a structured approach to data analysis using the Polars library while maintaining code quality through automation.
