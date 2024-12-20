import pandas as pd

# Load the dataset
file_path = "C:\Users\Hp\Downloads\archive (3)\Life Expectancy Data.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

# General information about the dataset
print(data.info())

# Summary statistics
print(data.describe())

# Checking for missing values
print(data.isnull().sum())

if 'Life expectancy' in data.columns:
    avg_life_expectancy = data['Life expectancy'].mean()
    print(f"Average Life Expectancy: {avg_life_expectancy:.2f}")
