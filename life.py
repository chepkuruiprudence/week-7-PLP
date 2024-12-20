import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import string
import warnings 
warnings.filterwarnings("ignore")

try:
    # Load the dataset
    df = pd.read_csv(r'C:\Users\Hp\Desktop\week-7-PLP\Life Expectancy Data.csv')
    print("Dataset loaded successfully!")

     # Print the head
    df.head()

     # Print the tail
    df.tail()

    # Show datatypes
    df.dtypes

    # show null values
    df.isnull().sum()

     # fill null values
    df_filled = df.fillna(df.mode().iloc[0])

     # confirm null values filled
    print(df_filled.isnull().sum())

     # print mean, median, mode
    df.describe()
    print(df)
    
    #remove panctuations
    df['cleaned_life_expectancy '] = df['Life expectancy '].astype(
        str).str.replace('[{}]'.format(string.punctuation), '', regex=True)
    
    #shoe cleand head
    print(df[['Life expectancy ', 'cleaned_life_expectancy ']].head())

except FileNotFoundError:
    print("Dataset not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")
    
#plot line graph
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Life expectancy ', hue='Country')
plt.title('Trends in Life Expectancy Over Time')
plt.xlabel('Year')
plt.ylabel('Life Expectancy ')
plt.legend(title='Country')
plt.grid(True)
plt.savefig('line_chart_life_expectancy.png')
plt.show()

#scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='GDP', y='Life expectancy ', hue='Country')
plt.title('Relationship Between GDP and Life Expectancy')
plt.xlabel('GDP')
plt.ylabel('Life Expectancy ')
plt.legend(title='Country')
plt.grid(True)
plt.savefig('scatter_plot_gdp_life_expectancy.png')
plt.show()

#bar chat
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Status', y='Life expectancy ', ci=None)
plt.title('Average Life Expectancy Across Status')
plt.xlabel('Status')
plt.ylabel('Average Life Expectancy ')
plt.savefig('bar_chart_life_expectancy.png')
plt.show()

#Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Life expectancy ', kde=True)
plt.title('Distribution of Life Expectancy')
plt.xlabel('Life Expectancy ')
plt.ylabel('Frequency')
plt.savefig('histogram_life_expectancy.png')
plt.show()

# Observations
print("""
Observations:
1. Life expectancy trends over the years show significant variation across countries.
2. Countries with higher GDP generally have higher life expectancy.
3. The distribution of life expectancy shows that most values are concentrated around a specific range.
4. Life expectancy varies between developed and developing countries.
""")



















