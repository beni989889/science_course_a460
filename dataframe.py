import pandas as pd

# data = {
#     'Name': ['Dana', 'Lior', 'Roni'],
#     'Score': [88, 92, 79],
#     'Passed': [True, True, False]
# }

# df = pd.DataFrame(data)
# # print(df.iloc[0])
# # print(df.iloc[1])
# print(df.head(2))

# dic_1={
#     'name':['dana','lior','roni'],
#     'age':['14','15','13'],
#     'city':['ashdod','tel aviv','haifa']
# }
# df=pd.DataFrame(dic_1)
# print(df)
# print(df.shape)

# import sqlite3
# import pandas as pd 
# conn = sqlite3.connect("chinook.db")
# # print(type(conn))
# query = "SELECT name from sqlite_master where type='table';"
# df = pd.read_sql(query,conn)
# print(df)


# query = "SELECT * from employees ;"
# df = pd.read_sql(query,conn)
# print(df)

# query = "SELECT * from invoices ;" 
# df = pd.read_sql(query,conn, index_col='InvoiceId')
# print(df)


import pandas as pd
import numpy as np

df = pd.DataFrame({
    "First_Name ": [" Alice", "bob ", "CHARLIE", None, "Diana"],
    "Last_Name": ["cohen", " Levy", "Smith ", "Brown", None],
    "Age": ["25", " thirty", "40", None, "22"],
    "Salary_USD": ["5000", "7000", "not available", "6200", None],
    "City_Name": ["Tel_aviv", "tel aviv", "Jerusalem", "Haifa", " haifa "],
    "Join_Date": ["2021-01-05", "2020-13-40", None, "2019-03-10", "2021/07/15"]
})

# df.info()
df.columns = df.columns.str.strip().astype(str).str.lower().str.replace("_"," ")
df["city name"]=df["city name"].str.strip().astype(str).str.lower().str.replace("_"," ")
df["first name"]=df["first name"].str.strip().astype(str).str.lower().str.replace("_"," ")
df["age"]= df["age"].str.strip().replace("thirty","30")
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["age"]=pd.to_numeric(df["age"], errors="coerce")
df["salary usd"]=df["salary usd"].str.strip().replace("not available",np.nan)
df["salary usd"]=pd.to_numeric(df["salary usd"], errors="coerce")
df["join date"]= pd.to_datetime(df["join date"],errors="coerce")
df.info()
print(df.isnull())
# df.fillna('/',inplace=True)
df["full name"]=df["first name"]+" "+ df["last name"]
print(df)
print(df.describe())

print(df.iloc[0:2])
print(df.iloc[0:3])
print(df.iloc[2])
print(df.iloc[0:5,0:4])
print(df.iloc[:,[1,2,3]])

print(df.loc[df["first name"].isin(['alice','bob'])])
df=df.set_index('first name')
print(df.loc['alice':'diana'])
df.loc["charlie",'salary usd']=7500
df.loc['charlie', 'salary usd'] = 7500
print(df.loc['charlie'])
print(df.loc[df["age"]>=30])## work only if disabled line 65!