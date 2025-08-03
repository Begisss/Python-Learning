import pandas as pd

df = pd.read_csv("sales_data.csv")

category_stats = df.groupby('Category').agg(
    Total_Quantity_Sold=('Quantity', 'sum'),
    Average_Price_Per_Unit=('Price', 'mean'),
    Max_Quantity_Sold_Single_Transaction=('Quantity', 'max')).reset_index()

print("=== Aggregate Statistics by Category ===")
print(category_stats)

top_selling_products = df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_selling_products = top_selling_products.sort_values(['Category', 'Quantity'], ascending=[True, False])
top_selling_by_category = top_selling_products.groupby('Category').first().reset_index()

print("\n=== Top-Selling Product in Each Category ===")
print(top_selling_by_category)

df['Total_Sale'] = df['Quantity'] * df['Price']
total_sales_by_date = df.groupby('Date')['Total_Sale'].sum().reset_index()
highest_sales_date = total_sales_by_date.sort_values('Total_Sale', ascending=False).head(1)

print("\n=== Date with Highest Total Sales ===")
print(highest_sales_date)


import pandas as pd

df = pd.read_csv("customer_orders.csv")

orders_per_customer = df.groupby('CustomerID').size().reset_index(name='OrderCount')
active_customers = orders_per_customer[orders_per_customer['OrderCount'] >= 20]
print("=== Customers with 20 or more orders ===")
print(active_customers)

avg_price_per_customer = df.groupby('CustomerID')['Price'].mean().reset_index(name='AvgPrice')
high_value_customers = avg_price_per_customer[avg_price_per_customer['AvgPrice'] > 120]
print("\n=== Customers with average price per unit > $120 ===")
print(high_value_customers)

product_totals = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Price', 'sum')).reset_index()

filtered_products = product_totals[product_totals['Total_Quantity'] >= 5]
print("\n=== Products with total quantity >= 5 ===")
print(filtered_products)


import pandas as pd
import sqlite3
import numpy as np

conn = sqlite3.connect("task/population.db")
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

salary_bands_df = pd.read_excel("task/population salary analysis.xlsx")

# Assumes columns are: 'Band', 'MinSalary', 'MaxSalary'
# Rename for consistency
salary_bands_df.columns = ['Band', 'MinSalary', 'MaxSalary']

def get_salary_band(salary):
    for _, row in salary_bands_df.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['Band']
    return 'Unknown'

population_df['SalaryBand'] = population_df['Salary'].apply(get_salary_band)

band_stats = population_df.groupby('SalaryBand').agg(
    Population_Count=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')).reset_index()

total_population = len(population_df)
band_stats['Percentage_of_Population'] = (band_stats['Population_Count'] / total_population) * 100

state_band_stats = population_df.groupby(['State', 'SalaryBand']).agg(
    Population_Count=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')).reset_index()

state_totals = population_df.groupby('State')['Salary'].count().reset_index(name='State_Total')

state_band_stats = state_band_stats.merge(state_totals, on='State')
state_band_stats['Percentage_of_Population'] = (
    state_band_stats['Population_Count'] / state_band_stats['State_Total'] * 100)
state_band_stats.drop(columns='State_Total', inplace=True)

print("=== Global Salary Band Statistics ===")
print(band_stats)

print("\n=== State-wise Salary Band Statistics ===")
print(state_band_stats)

