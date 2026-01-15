import pandas as pd
# df=pd.read_csv('students.csv' ,header=2)
# print(df)
# print(df.iloc[0])

# url = "https://raw.githubusercontent.com/kirenz/datasets/master/height.csv"
# df2 = pd.read_csv(url,usecols=['name','height'])
# print(df2)

url_excel = "https://github.com/bharathirajatut/sample-excel-dataset/raw/master/airline.xls"
df3= pd.read_excel(url_excel)
print(df3)
