import pandas as pd
# index_1=['a','b','c','d','e','f','g','h','i','j']
# s1=pd.Series([10,20,30,40,50,60,70,80,90,100],index=index_1)
# print(s1)

# dic_1={
#     'apple': "red",
#     "banna":"yellow",
#     "grape":"purple",
# }

# s2=pd.Series(dic_1)
# print(s2)

# grades=pd.Series([88,92,79,95],index=['alice','bob','charlie','david'])
# print("charlie's grade:",grades['charlie'])
# grades['charlie']=85
# print("charlie's updated grade:",grades['charlie'])

#1
s1=pd.Series([10,20,30])
#2
s1=pd.Series([10,20,30],index=['a','b','c'])
#3
print(s1[1])
#4
print(s1['b'])
#5
dic_1={
    'apple':"40",
    'banna':"20",
    'grape':"30",
    'orange':"50",
}
s2=pd.Series(dic_1)
print(s2)
#6
s1=pd.Series(4,index=['a','b','c','d'])
print(s1)
#7
s1=pd.Series([10,20,30])
print(s1[1:3])
#8
max_than=s1>15
print(s1[max_than])
print(s1[s1>15])
#9
