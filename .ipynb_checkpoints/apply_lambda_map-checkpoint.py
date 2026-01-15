import pandas as pd
import numpy as np

df = pd.DataFrame({
    'first_name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eli'],
    'last_name': ['Smith', 'Jones', 'Brown', 'Taylor', 'White'],
    'age': [25, 17, 35, 16, 28],
    'salary': [5000, 4000, 7000, 3000, 6500],
    'bonus': [500, 200, 700, 100, 600],
    'department': ['HR', 'IT', 'Sales', 'HR', 'IT']
})
#1
df['first_name']=df['first_name'].str.upper()
# # print(df)
# #2
def plus_rows(row):
    return row['first_name']+ ' ' +row['last_name']
df['full_name']=df.apply(plus_rows,axis=1)

# #3
df['age']= df['age'].map(lambda x:x+5)

# #4
df['is_adult']=df['age'].apply(lambda x: x>18)
# print(df)
#5



import pandas as pd

orders_full = pd.DataFrame({
    "OrderID": [101, 102, 103, 104],
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Quantity": [1, 2, 1, None],
    "Country": ["USA", "UK", "UK", "Canada"],
    "Status": ["Delivered", "Delivered", "Cancelled", None]
})
print(orders_full)
status_map = {
    "Delivered": "Delivered ✅",
    "Cancelled": "Cancelled ❌"
}

# #"Pending ⏳"
orders_full['Status'] = orders_full['Status'].map(status_map).fillna("Pending ⏳")
# print(orders_full)



