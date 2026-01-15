full_name=input("enter your name:")
#id_number=input("enter your id number exactly 9 numberes:")
#phone_number=input("enter your phone number 05xxxxxxxx:")
split_name=full_name.split()
if split_name[0].upper()==split_name[0]:  
     if split_name[2].upper()==split_name[2]:
          print("good name ")
     else:
          print("name not good")


'''
import math
print(divmod(50,8))
print(math.fabs(-7.5))


price = 49.9
message = "The total is " + str(round(price * 1.17, 2))
print(abs(0))
print(math.sqrt(25))
x=5
print(f"the value is {x}")
x= "banna"
y= "apple"
print(x.replace("banna","apple"))

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)
'''