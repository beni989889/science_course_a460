import pandas as pd


data = {

    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108],

    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eli', 'Fay', 'George', 'Hana'],

    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],

    'HourlyWage': [50, 65, 55, 70, 52, 60, 68, 53],

    'MonthlyHours': [160, 150, 170, 180, 155, 165, 175, 160],

    'Remote': [True, False, True, False, True, True, False, True]

}


df = pd.DataFrame(data)

print(df['HourlyWage'].agg(['mean','max','min']))

print((df['HourlyWage']*df['MonthlyHours']).max())

