t1=(5,10,15,20,25)
for item in t1:
    if item==15:
        print("Found 15!")
        break
print(t1[2])

colors = ("red", "green", "blue", "yellow")
print(len(colors))

nums = (1, 2, 3)
list1=list(nums)
list1.append(4)
list1=tuple(list1)
print(list1)

point = (4, 7)
x,y=point
print(f"x: {x}, y: {y}")

t = (10, 20, 30, 40, 50, 60)
print(t[1:4])

letters = ("a", "b", "c", "d", "e")
for letter_d in range(len(letters)):
    if letters[letter_d] == "d":
        print(f"found d at index {letter_d}")
print(letters.index("d"))
#7
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple3=tuple1+tuple2
print(tuple3)
#8
set1={1, 2, 2, 3, 4, 4, 5}
print(set1)
#9
items=set()
items.add("apple")
items.add("banna")
items.add("orange")
items.remove("banna")
print(items)
#10
names = {"Noa", "Lior", "Dana"}
if "Lior" in names:
    print("Lior is in the set")
else:
    print("Lior is not in the set")


