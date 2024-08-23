###1. Importing the dataset using pandas

#using pandas to import data from csv file

import pandas as pd

# Importing the dataset

product_data = pd.read_csv('Product_Detail.csv')
sale_data = pd.read_csv('sale_data.csv')

# Displaying the dataset

print(product_data)

#------------------------------------------------------------------------------------------#
###2. Cleaning the data

# Remove duplicate rows
product_data = product_data.drop_duplicates()

# Fill missing values in 'product_description' column with 'Null'
product_data['product_description'] = product_data['product_description'].fillna('Null')

# Convert 'Sale_Date' column to datetime format
sale_data['Sale_Date'] = pd.to_datetime(sale_data['Sale_Date'])

# Drop rows where 'product_stock' is missing
product_data = product_data.dropna(subset=['product_stock'])

# Display cleaned data
print(product_data.head())
print(sale_data.head())


#------------------------------------------------------------------------------------------#

###3. Data Preprocessing


#Preprocess data to prepare it for analysis. This might include normalizing data, creating new features, or merging datasets.

# Merge product_data and sale_data on 'product_id'
merged_data = pd.merge(product_data, sale_data, on='product_id', how='inner')

# Calculate total sales for each product
merged_data['total_sales'] = merged_data['product_price'] * merged_data['Quantity']

# Calculate total sales for all products
total_sales = merged_data['total_sales'].sum()

# Display preprocessed data
print(merged_data)

#Print total sales

print('Total Sales:', total_sales , 'USD')
#------------------------------------------------------------------------------------------#

###4. Applying Pandas for data cleaning and preprocessing

import pandas as pd

# Load data
df = pd.read_csv('sales_data.csv')

# Handle missing data
df.fillna(method='ffill', inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date column to datetime
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])


#------------------------------------------------------------------------------------------#

###5. Data Visualization

# Importing the required libraries
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Plotting a bar chart for total sales by product category
plt.figure(figsize=(10, 6))
sns.barplot(x='product_category', y='total_sales', data=merged_data)
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45)
plt.show()


# Using matplotlib to plot a line chart for total sales over time
plt.figure(figsize=(10, 6))
plt.plot(merged_data['Sale_Date'], merged_data['total_sales'])
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45)
plt.show()
