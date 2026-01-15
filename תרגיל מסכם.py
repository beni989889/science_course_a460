import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
print(os.getcwd())

candy_factories = pd.read_csv("Candy_Factories.csv")
print(candy_factories.head(3))
candy_products = pd.read_csv("Candy_Products.csv")
print(candy_products.head(3))
customers = pd.read_csv("Customers.csv")
print(customers.head(3))
sales_us = pd.read_csv("Sales_US.csv")
print(sales_us.head(3))
sales_ca = pd.read_csv("Sales_CA.csv")
print(sales_ca.head(3))
candy_targets = pd.read_json("Candy_Targets.json")
print(candy_targets.head(3))
print("////////")

print(f"candy_factories{candy_factories.tail(3)}")
print(f"candy_products{candy_products.tail(3)}")
print(f"customers{customers.tail(3)}")
print(f"sales_us{sales_us.tail(3)}")
print(f"sales_ca{sales_ca.tail(3)}")
print(f"candy_targets{candy_targets.tail(3)}")

print(f"candy_factories{candy_factories.shape}{candy_factories.info}{candy_factories.describe()}")
print(f"candy_products{candy_products.shape}{candy_products.info}{candy_products.describe()}")
print(f"customers{customers.shape}{customers.info}{customers.describe()}")
print(f"sales_us{sales_us.shape}{sales_us.info}{sales_us.describe()}")
print(f"sales_ca{sales_ca.shape}{sales_ca.info}{sales_ca.describe()}")
print(f"candy_targets{candy_targets.shape}{candy_targets.info}{candy_targets.describe()}")

def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    return df

candy_factories = clean_column_names(candy_factories)
candy_products = clean_column_names(candy_products)
customers = clean_column_names(customers)
sales_us = clean_column_names(sales_us)
sales_ca = clean_column_names(sales_ca)
candy_targets = clean_column_names(candy_targets)

shipping_dict = {
    'First Class': 10,
    'Second Class': 5,
    'Standard Class': 3,
    'Same Day': 20
}
sales_ca['shipping_cost']=sales_ca['ship_mode'].map(shipping_dict)
sales_us['shipping_cost']=sales_us['ship_mode'].map(shipping_dict)
# print(sales_ca[['ship_mode','shipping_cost']].head(3))

sales_us['rank_sales']=sales_us['sales'].apply(lambda x: 'high' if x>200 else 'medium' if 50<= x <=200 else 'low')
# print(sales_us[['sales','rank_sales']].head(7))

print(sales_ca.columns)
print(sales_us.columns)

sales_ca['total_cost']=sales_ca['price_per_unit']*sales_ca['units']
print(sales_ca[['price_per_unit','units','total_cost']].head(3))

sales_us['year_date']=pd.DatetimeIndex(sales_us['order_date']).year
sales_ca['year_date']=pd.DatetimeIndex(sales_ca['order_date']).year
print(sales_us[['order_date','year_date']].head(3))

print(sales_ca.columns)
print(sales_us.columns)

#הנחה של 10% על כל הזמנה של יותר מ-5 יחידות
sales_ca['total_cost']= sales_ca.apply(lambda x: x['total_cost'] - (x['total_cost']*0.1) if x['units']>5 else x['total_cost'] ,axis=1)
print(sales_ca[['units','total_cost']].head(7))

customers['address']=customers['address'].fillna('No address provided')
print(customers[['customer_id','address']].head(15))

#הגדרת עמודות של תאריך כערך של תאריך.
sales_ca['order_date']=pd.to_datetime(sales_ca['order_date'])
sales_us['order_date']=pd.to_datetime(sales_us['order_date'])
sales_ca['year_date']=pd.to_datetime(sales_ca['year_date'])
sales_us['year_date']=pd.to_datetime(sales_us['year_date'])
sales_ca['ship_date']=pd.to_datetime(sales_ca['ship_date'])
sales_us['ship_date']=pd.to_datetime(sales_us['ship_date'])

# print(sales_us.info())

#מיזוג טבלאות מכירות של ארה"ב וקנדה
sales_new=pd.concat([sales_us,sales_ca],ignore_index=True)
print(sales_new.head(10))

#מיזוג טבלת מכירות עם טבלת לקוחות
merged_data = sales_new.merge(customers , on='customer_id', how='inner')
print(merged_data.head(10))

print(merged_data.columns)
#שינוי שם עמודה של גיל לקוח
merged_data= merged_data.rename(columns={'age': 'customer_age'})
print(merged_data['customer_age'].head(3))
print(merged_data.columns)
#יצירת עמודה חדשה של עיר מתוך עמודת כתובת
merged_data['city_new'] = ( merged_data['address'].str.split(',').str[-1].str.strip())
print(merged_data[['address','city_new']].head(7))

merged_data['address'] = merged_data.apply(lambda row: row['address'].replace(row['city_new'], '').strip(),axis=1)
merged_data['address'] = merged_data['address'].str.rstrip(', ').str.strip()
print(merged_data[['address','city_new']].head(7))
#מודא שcustomer_id מופיע פעם אחת
merged_data= merged_data.drop_duplicates(subset=['customer_id'])
print(merged_data['customer_id'].is_unique)
#הצגת עמודות נבחרות
print(merged_data.loc[:,['customer_id','product_name','units','total_cost']].head(10))
#הצגת שורות ועמודות נבחרות
print(merged_data.iloc[0:5, 2:6])
#הצגת שורות לפי תנאי
print(merged_data.loc[(merged_data['units']>3) | (merged_data['total_cost']>20), ['product_name','total_cost']])


