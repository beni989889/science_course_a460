'''
num1=1
while num1<=10:
    print(num1)
    num1+=1
'''
'''
even_num=2
while even_num<=20:
    print(even_num)
    even_num+=2
'''
# x=10#the ##loop forever
# while x>0 :
#     print(x)
#     x+=1

# while price != "stop": ##shopping cart
#    price = input("Enter product price or type stop")
#    if price!='stop':
#        count+=1
#        total+=float(price)

# print(f"Total of items: {count}")
# print(f"Total cost: {total}")

# sum_num=int(input("enter a number to sum it")) ##print the sum of all numbers from 1 to num
# new_one=0
# x=1
# while x<=sum_num:
#     new_one+=x
#     x+=1
# print(new_one)

# x=0
# while x<=10:
#     x+=1
#     if x==5 or x==8:
#         continue
#     print(x)

# start_num=int(input("enter a starting number:"))
# stop_num=int(input("enter a stopping number:"))
# for x in range(start_num,stop_num+1):
#         print(x)

# limit_num=int(input("enter your neme please"))
# sum_num=0
# for x in range (1,limit_num+1):
#   sum_num+=x
# print(sum_num)

# ask_num=int(input("enter a number to make mulitplaction table:"))
# for x in range(1,11):
#     print(ask_num*x)

# list1=[1,2,3,4,5,6]
# list1.reverse()
# print(list1)

# guess_word=(input("enter a word:")) ##print the word vertically
# for x in range(0,len(guess_word)):
#     print(guess_word[x])

# guess_word=(input("enter a word:")) ##count the vowels in a word
# counter=0
# for x in range(0,len(guess_word)):
#     if guess_word[x]=="a" or guess_word[x]=="e" or guess_word[x]=="i" or guess_word[x]=="o" or guess_word[x]=="u":
#         counter+=1
# print(counter)

# n_guess=int(input("enter your number")) ##calculate factorial
# factorial=1
# for x in range(1,n_guess+1):
#     factorial*=x
# print(factorial)

# rows=int(input("enter number of rows:")) ##print star triangle
# columns=int(input("enter number of colums:"))
# for x in range(1,rows+1):
#   print("*"*columns)

# trangle_size=int(input("enter size of triangle:")) ##print star triangle
# for x in range(1,trangle_size+1):
#     print("*"*x)
# import math
# n_number=int(input("enter your new number")) ##print all prime numbers up to n_number
# for x in range(2,n_number):
#     if(x


# fruit= []
# fruit.append("apple")
# fruit.append("banana")


# list1=[10,20,30,40,50]
# for x in list1:
#     print(x)

# list2="banana"
# y=0
# for x in list2:
#     if x=="a":
#         y+=1
# print(y)

# list1=[10,20,30,40,50,60,70,80,90,100] ##calculate average of numbers in a list
# sum=0
# count=0
# for x in list1:
#     sum+=x
#     count+=1
# print(sum/count)

# list1=[3,5,30,40,50,60,70,80,90,100] 
# for x in list1:
#     if x%2==0:
#         print(x)

# list1=[3,5,30,40,50,60,70,80,90,100]
# list2=[]
# for x in list1:
#     list2.append(x*2)
# print(list2)

#list1=input("enter numbers separated by space:").split()
# list2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for i,index in enumerate(list2):
#     if index>10:
#         print(index)

# list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for i,n in enumerate(list1):
#     if i%2==0:
#         print(n)

# list1=[1,2,3,4,5,6,7,8,9,10]
# new1=[x+1 for x in list1]
# print(new1)

# list1=[1,2,3,4,5]
# list2=[x*x for x in list1]
# print(list2)

# new_str=str(input("enter your string:"))
# new_list=new_str.split()
# new_joined="_".join(new_list)
# print(new_joined)

# for x in range(1,4):  ##print star pattern
#     for y in range(1,4):
#         print("*",end=" ")
#     print()

# for x in range(1,6):
#     for y in range(1,6):
#         print(y*x,end=" ")
#     print()

# matrix= [[5,8,2],[3,9,4],[1,6,7]]
# book1=False
# for row in matrix:
#     if book1:
#         break
#     for item in row:
#         if item==8:
#             print(row.index(item),matrix.index(row))
#             book1=True
#             break
    

# my_list=[1,2,3]
# # my_list+= [4,5]
# my_list.append(4,5)
# print(my_list)

# my_list=[1,h,3,4,b,w]
# print(my_list)

# print(type(range(5)))

# my_1=[one,two, three]
# sr=my_1.split()
# print(sr)

# txt=" python is fun"
# x=txt.split()
# part= "-".join(x)
# print(part)

# matrix= [[1,2,3],[4,5,6],[7,8,9]]
# # print(matrix[1][2])
# print(matrix[1][2])
x="she said \"hello\" to me"
print(x.find("hello"))

