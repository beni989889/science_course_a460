try:    #מציג טיפול בשגיאה מסוג TypeError
    string1="15"
    num1=15
    result= num1 + string1
    print("Result:", result)
except TypeError :
   print("Caught a TypeError: Cannot add str and int")

try:
    num = int("abc") 
    print("Converted number:", num)
except ValueError:
    print("Invalid conversion!")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range!")

try:
    d = {"a": 1, "b": 2}
    print(d["c"])
except KeyError:
    print("Key not found in dictionary!")

try:
    x = 10
    x.append(5)
except AttributeError:
    print("Attribute not found!")





