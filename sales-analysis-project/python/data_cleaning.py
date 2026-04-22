import pandas as pd

df = pd.read_csv("superstore.csv", encoding = "latin1")

print(df.head().to_string())
print(df.tail().to_string())
print(df.columns)
# print(df.shape)

# data cleaning
print(df.isnull().sum()) # checking missing values
df = df.dropna() # removing missing values

# converting, creating columns
df["Order Date"] = pd.to_datetime(df["Order Date"], errors = "coerce")
df = df.dropna(subset=['Order Date'])
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Profit Margin"] = df["Profit"] / df["Sales"]
print(df.head().to_string())

# data analysis
print("Total Sales: ", df["Sales"].sum())
print("Total Profit: ", df["Profit"].sum())
print(df.groupby("Region")["Sales"].sum())
print(df.groupby("Category")["Profit"].sum())
print(df.groupby(['Year', 'Month'])['Sales'].sum())
print(df.shape)

# saving cleaned data
df.to_csv("cleaned_sales_data_final.csv", index = False, encoding = "utf-8")
