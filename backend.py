"""
@Author:Ayesha Ali
A backend script to process the data the databases and write the data in Test task - Orders.csv and get JSON data for that csv file.
Assumptions: In Test task - Mongo - customers.csv, company name corresponds to company id which in turn corresponds to user_id
order_id in Test task - Postgres - deliveries.csv corresponds to id in Test task - Orders.csv which is used to fing total amount and product name for each order
order_item in Test task - Postgres - deliveries.csv corresponds to id in Test task - Orders.csv which is used find the delivered amount
"""
import pandas as pd
import numpy as np
mongo1 = pd.read_csv('Test task - Mongo - customer_companies.csv')
mongo2 = pd.read_csv('Test task - Mongo - customers.csv')
order = pd.read_csv('Test task - Orders.csv')
postgre1 = pd.read_csv('Test task - Postgres - deliveries.csv')
postgre2 = pd.read_csv('Test task - Postgres - order_items.csv')
columns = ['Order Name', 'Customer Company', 'Customer Name', 'Order Date','Delivered Amount','Total Amount']
data = [mongo2["user_id"], mongo2["name"], mongo2["company_id"],  mongo1["company_name"]]
headers = ["user_id", "name", "company_id", "company_name"]
df3 = pd.concat(data, axis=1, keys=headers)
companies = []
# Select column contents by column name using [] operator
columnSeriesObj = order['customer_id']
for i in range(len(columnSeriesObj.values)):
    if columnSeriesObj.values[i] in df3['user_id'].values:
        index = df3.index[columnSeriesObj.values[i] == df3['user_id'].values]
        columnSeriesObj.values[i] = df3['name'].values[index]
        companies.append(df3['company_name'].values[index])
order["Company Name"] = companies
#update price per quantity and product name
postgre2 = postgre2.fillna(0)
order["Total Amount"] = 0.0
order["Product Names"] = " "
price = postgre2['price_per_unit'].values
quantity = postgre2['quantity'].values
for i in range(len(price)):
    index = order.index[postgre2['order_id'].values[i] == order['id'].values]
    #print(order["Total Amount"].values[index])
    order["Total Amount"].values[index] += price[i] * quantity[i]
    if order["Product Names"].values[index] == " ":
        order["Product Names"].values[index] += postgre2["product"].values[i]
    else:
        order["Product Names"].values[index] += "," + postgre2["product"].values[i]
#update delivered amount
order["Delivered Amount"] = 0.0
delivered = postgre1['delivered_quantity'].values
for i in range(len(delivered)):
    index1 = postgre2.index[postgre1['order_item_id'].values[i] == postgre2['id'].values]
    index2 = order.index[postgre2['order_id'].values[index1] == order['id'].values]
    order["Delivered Amount"].values[index2] += delivered[i] * postgre2['price_per_unit'].values[index1]
order = order.rename(columns={'customer_id': 'customer_name'})
order["created_at"] = order["created_at"].apply(lambda x: x[0:10])
order.to_csv('Test task - Orders.csv')
order = pd.read_csv('Test task - Orders.csv')
order["customer_name"] = order["customer_name"].apply(lambda x: x.strip("[']"))
order["Company Name"] = order["Company Name"].apply(lambda x: x.strip("[']"))
order = order.rename(columns={'Total Amount': 'total_amount'})
json = order.to_json(orient='records')
print(json.total_amount)
order.to_csv('Test task - Orders.csv')




