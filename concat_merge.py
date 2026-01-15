import pandas as pd

df_hr = pd.DataFrame({
    'EmployeeID': [101, 102],
    'Name': ['Alice', 'Bob'],
    'Department': ['HR', 'HR']
})

df_it = pd.DataFrame({
    'EmployeeID': [103, 104],
    'Name': ['Charlie', 'Diana'],
    'Department': ['IT', 'IT']
})

df_salary = pd.DataFrame({
    'EmployeeID': [101, 102, 103],
    'Salary': [5000, 5500, 6000]
})

df_combined= pd.concat([df_hr,df_it],ignore_index=True,axis=0)
# print(df_combined)

df_combined2=pd.concat([df_salary,df_it],axis=1)
# print(df_combined2)

import pandas as pd

# # Customers table
customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Country": ["USA", "UK", "USA", "Canada"],
    "JoinDate": ["2021-01-15", "2020-05-20", "2019-08-10", "2021-03-01"]
})

# # Orders table
orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104],
    "CustomerKey": [1, 2, 2, 5],
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Quantity": [1, 2, 1, 1]
})

# # Shipping table
shipping = pd.DataFrame({
    "OrderRef": [101, 102, 103, 105],
    "ShipDate": ["2021-02-01", "2020-06-01", "2020-06-15", "2021-04-01"],
    "Status": ["Delivered", "Delivered", "Cancelled", "Delivered"]
})

df_merged= pd.merge(customers,orders,left_on="CustomerID",right_on="CustomerKey",how='left')

import pandas as pd


df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Tel Aviv', 'Jerusalem', 'Haifa']
})


df2 = pd.DataFrame({
    'Name': ['Diana', 'Eve', 'Frank'],
    'Age': [28, 22, 40],
    'City': ['Beer Sheva', 'Rishon Lezion', 'Ashdod']
})

#1
df_combined=pd.concat([df1,df2],ignore_index=True,axis=0)
# print(df_combined)
#2
df_combined=pd.concat([df1,df2],ignore_index=True,axis=1)
# print(df_combined)
#3
df_combined=pd.concat([df1,df2],ignore_index=True,axis=0)
# print(df_combined)
#4
df_combined=pd.concat([df1,df2],axis=0,keys=['A','B'])
# print(df_combined)
# #5
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})
# print(df1)
df2 = pd.DataFrame({
    'Name': ['Diana', 'Eve', 'Frank'],
    'City': ['Beer Sheva', 'Rishon Lezion', 'Ashdod']
})
# print(df2)
df_combined=pd.concat([df1,df2],axis=0)
# print(df_combined)


df_students = pd.DataFrame({
    "StudentID": [201, 202, 203, 204, 205],
    "FirstName": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "LastName": ["Smith", "Brown", "Johnson", "Miller", "Davis"],
    "Major": ["Math", "Physics", "Chemistry", "Biology", "History"],
    "Age": [20, 22, 21, 23, 20]
})

df_grades = pd.DataFrame({
    "course_id": [301, 302, 303, 304, 305, 306],
    "student_id": [201, 203, 202, 201, 204, 206],
    "course_name": ["Algebra", "Physics I", "Chemistry I", "Calculus", "Biology I", "History I"],
    "grade": [95, 88, 76, 89, 92, 85]
})

#6
df_merged = pd.merge(df_students, df_grades, left_on="StudentID", right_on="student_id",how='inner')
print(df_merged)
#7
df_merged = pd.merge(df_students, df_grades, left_on="StudentID", right_on="student_id",how='left')
print(df_merged)
#8
df_merged = pd.merge(df_students, df_grades, left_on="StudentID", right_on="student_id",how='right')
print(df_merged)
#9
df_merged = pd.merge(df_students, df_grades, left_on='StudentID', right_on='student_id', how='outer')
print(df_merged)
#10
df1 = pd.DataFrame({
    'first_name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'last_name': ['Cohen', 'Smith', 'Brown', 'Levy'],
    'age': [25, 30, 35, 28]
})

df2 = pd.DataFrame({
    'first_name': ['Alice', 'Bob', 'Charlie', 'Eve'],
    'last_name': ['Cohen', 'Smith', 'Brown', 'Adams'],
    'city': ['Tel Aviv', 'Jerusalem', 'Haifa', 'Beer Sheva']
})
df_merged = pd.merge(df1, df2, on=['first_name', 'last_name'], how='outer')
print(df_merged)
#11
df1 = pd.DataFrame({
    'emp_id': [101, 102, 103, 104],
    'first_name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28]
})


df2 = pd.DataFrame({
    'employee_id': [101, 102, 105, 106],
    'department': ['HR', 'IT', 'Finance', 'Marketing'],
    'city': ['Tel Aviv', 'Jerusalem', 'Haifa', 'Beer Sheva']
})

df_merged = pd.merge(df1, df2, left_on='emp_id', right_on='employee_id', how='inner')
print(df_merged)
#12

df1 = pd.DataFrame({
    'first_name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'last_name': ['Cohen', 'Smith', 'Brown', 'Levy'],
    'age': [25, 30, 35, 28]
})

df2 = pd.DataFrame({
    'first_name': ['Alice', 'Bob', 'Charlie', 'Eve'],
    'last_name': ['Cohen', 'Smith', 'Brown', 'Adams'],
    'city': ['Tel Aviv', 'Jerusalem', 'Haifa', 'Beer Sheva']
})

df_merged = pd.merge(df1, df2, left_on='first_name', right_on='first_name', how='outer', suffixes=('_left', '_right'))
print(df_merged)
#13indicator

df_merged = pd.merge(df1, df2, on='first_name', how='outer', indicator=True)
print(df_merged)

#14Concatenate a List of DataFrames Given a list [df1, df2, df3], concatenate all DataFrames vertically in one line.
df3 = pd.DataFrame({
    'first_name': ['Frank', 'Grace'],
    'last_name': ['Wright', 'Hall'],
    'age': [40, 32]
}) 
df_combined = pd.concat([df1, df2, df3], ignore_index=True, axis=0)
print(df_combined)



