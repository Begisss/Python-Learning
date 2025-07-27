import pandas as pd
import numpy as np 
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    }
df = pd.DataFrame(data)
df.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True)

print("First 3 rows:")
print(df.head(3))

mean_age = df['age'].mean()
print("\nMean age:", mean_age)

print("\nSelected columns (first_name and city):")
print(df[['first_name', 'city']])

df['salary'] = np.random.randint(50000, 100001, size=len(df))

print("\nSummary statistics:")
print(df.describe())


import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print("\nMinimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print("\nAverage Sales:", avg_sales)
print("Average Expenses:", avg_expenses)


import pandas as pd
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170,],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)
expenses = expenses.set_index('Category')

print("Maximum expense for each category:")
print(expenses.max(axis=1))

print("\nMinimum expense for each category:")
print(expenses.min(axis=1))

print("\nAverage expense for each category:")
print(expenses.mean(axis=1))
