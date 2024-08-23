# Importing the required libraries
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Load data
product_data = pd.read_csv('Product_Detail.csv')
sale_data = pd.read_csv('sale_data.csv')
product_group = pd.read_csv('product_group.csv')

# Merge product_data and sale_data on 'product_id'
merged_data = pd.merge(product_data, sale_data, on='product_id', how='inner')
merged_data = pd.merge(merged_data, product_group, on='product_group_id', how='inner')

# Calculate total sales for each product
merged_data['total_sales'] = merged_data['product_price'] * merged_data['Quantity']

# Plotting a bar chart for total sales by product category
plt.figure(figsize=(10, 6))
sns.barplot(x='product_name', y='total_sales', data=merged_data)
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45)
plt.show()

# Plotting a line chart for total sales over time by date
plt.figure(figsize=(10, 6))
plt.plot(merged_data['Sale_Date'], merged_data['total_sales'])
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45)
plt.show()


# Assuming merged_data is already loaded

# Convert 'Sale_Date' to datetime
merged_data['Sale_Date'] = pd.to_datetime(merged_data['Sale_Date'], errors='coerce')

# Check for NaT (not a time) values that could indicate invalid dates
if merged_data['Sale_Date'].isnull().any():
    print("Warning: Some dates could not be parsed and were converted to NaT.")

# Group by month and sum total sales
monthly_sales = merged_data.groupby(merged_data['Sale_Date'].dt.month)['total_sales'].sum()

# Display monthly sales
print(monthly_sales)

# Plotting a line chart for total sales by month
plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales (USD)')
plt.xticks(range(1, 13))
plt.show()
