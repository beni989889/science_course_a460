school_dic={
    "asaf_mimon":{
        "city":"ashkelon",
        "students": ["ron ozeri","dhlomo amsalem","yosef amoyal"] 
    },
    "sinai":{
        "city":"beersheva",
        "students": ["maor betito","benjamin benlulu","liav cohen","snir revivo"]
    },
    "madaim":{
        "city":"ashkelon",
        "students": ["or giladi","duriel levi","yair avivi"]
    }
}
# school_name=dict.keys(school_dic)
# print(school_name)
# print(dict.values(school_dic))
# print(school_dic["sinai"]["students"])
# print(dict.items(school_dic))

# for school,info in dict.items(school_dic):
#     if info["city"]=="ashkelon":
#         print(f"The school {school} is in ashkelon")
#         for student in info["students"]:
#             print(student)

school_dic["yeshivat tzvia"]={
        "city":"ashkelon",
        "students": ["harel vizman","hod buhnik","yehuda cohen"]
        }

# print(school_dic)

# school_dic["madaim"]["students"].append("david levi")
# school_dic["madaim"]["students"].remove("david levi")
# del school_dic["madaim"]
# print(school_dic)
# for school,info in dict.items(school_dic):
#     for student in info["students"]:
#         if startwith(student,'d'):
#             print(f"The students {info["students"]} is starts with d")

# for school,info in school_dic.items():
#      for student in info['students']:
#          first_name=student.split()[0]
#          if first_name.lower().startswith('d'):
#           print(f"The student that starts with D is: {student} (school: {school})")

# for school, info in school_dic.items():
#     for student in info["students"]:
#         if student.startswith('d'):
#             print(f"The student {student} starts with 'd'")

school_dic2={
    "yigal alom":{ 
        "city":"beersheva",
        "students":{
            "david levi":{
                "id_number":254876543,
                "age":17,
                "address":"herzel 10",
                "gender":"male"
            },
            "shira cohen":{
                "id_number":254876544,
                "age":16,
                "address":"herzel 12",
                "gender":"female"
            }
        }
    },
    "yeshivat tzvia":{ 
        "city":"ashkelon",
        "students":{
            "hod buhnik":{
                "id_number":254876545,
                "age":17,
                "address":"herzel 14",
                "gender":"male"
            }
        }
}
}

dic_1={
    'name': 'Alice',
    'age': 35,
    'city': 'New York'

}
dic_1['profession']='professor'
dic_1['age']=40
print(dic_1)
print(dic_1['city'])

del dic_1['profession']
print(dic_1)
print(dic_1.items())
for key in dic_1.keys():
    if key=='age':
        print(f"found age: {dic_1[key]}")

print('age' in dic_1)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dic=dict(zip(keys,values))
print(res_dic)

my_list = [10, 20, 30, 40, 50]
print(len(my_list))
my_list.clear()
# Write a code to check is list empty
if my_list:
    print("The list is not empty")
else:
    print("The list is empty")


my_list = [10, 20, 30, 40, 50]
my_list.append(600)
print(my_list)
my_list.insert(2,300)
print(my_list)
my_list.pop(0)
print(my_list)

numbers = [1, 2, 3, 4, 5, 6, 7]
for num in range(len(numbers)):
   numbers[num]=numbers[num]*numbers[num]
print(numbers)

list=[8, 2, 15, 1, 9]
print(max(list))
print(min(list))
