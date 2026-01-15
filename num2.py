full_name=input("ENTER your NAME") ###קבלת שם פרטי+שם משפחה ולבדוק האם הם מתחילים באות גדולה
split_name=full_name.split()
#print(split_name[0])
#print(split_name[1])
#print(split_name[2])
first, last=split_name
if first[0].isupper() and last[0].isupper():
    print("Good name")
else:
    print("Name not good")