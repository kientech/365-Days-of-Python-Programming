# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 14

# Data Analysis with Pandas
# This script requires the 'pandas' library:
# pip install pandas

import pandas as pd
import io

# Create a dummy CSV data string to simulate reading from a file
csv_data = """Name,Age,City,Salary
John,34,New York,80000
Anna,28,Paris,65000
Peter,42,London,120000
Linda,31,Tokyo,75000
Mike,25,New York,60000
"""

# Use io.StringIO to read the string data as if it were a file
data_file = io.StringIO(csv_data)

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(data_file)

print("--- Original DataFrame ---")
print(df)
print("\n" + "="*30 + "\n")

# --- Basic Data Analysis ---

# 1. Get a summary of the DataFrame
print("--- DataFrame Info ---")
df.info()
print("\n" + "="*30 + "\n")

# 2. Get descriptive statistics
print("--- Descriptive Statistics ---")
print(df.describe())
print("\n" + "="*30 + "\n")

# 3. Calculate the average salary
average_salary = df['Salary'].mean()
print(f"--- Average Salary ---\n${average_salary:.2f}\n")
print("\n" + "="*30 + "\n")

# 4. Filter data - find people older than 30
print("--- People Older Than 30 ---")
older_than_30 = df[df['Age'] > 30]
print(older_than_30)
print("\n" + "="*30 + "\n")

# 5. Group by city and calculate the average salary per city
print("--- Average Salary by City ---")
avg_salary_by_city = df.groupby('City')['Salary'].mean()
print(avg_salary_by_city) 