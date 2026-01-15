import random
'''פיתרון עם פונקציית if
num1=random.randint(1,20)
num2=int(input("enter a number between 1 and 20:"))
if num1==num2:
    print("correct")
elif num2>num1:
    print("lower")
    num2=int(input("enter a number between 1 and 20:"))
    if num1==num2:
        print("correct")
elif num2<num1:
    print("higher")
    num2=int(input("enter a number between 1 and 20:"))
    if num1==num2:
        print("correct")
if num1!=num2:
    print("the true number was", num1)
    num3=input("if you want to play again type yes:")
    if num3=="yes":
        num1=random.randint(1,20)
        num2=int(input("enter a number between 1 and 20:"))
        if num1==num2:
            print("correct")
        elif num2>num1:
            print("lower")
            num2=int(input("enter a number between 1 and 20:"))
            if num1==num2:
                print("correct")
        elif num2<num1:
            print("higher")
            num2=int(input("enter a number between 1 and 20:"))
            if num1==num2:
                print("correct")
        if num1!=num2:
            print("the true number was", num1)
    if num3!="yes":
        print("thank you for playing")
'''
random_number=random.randint(1,20)
guess_number=int(input("enter a number between 1 and 20:"))
counter=2
while counter>0:
    if guess_number==random_number:
        print("correct")
        break
    else:
        if counter!=1:
            counter-=1
            if guess_number>random_number:
                print("lower")
                guess_number=int(input("enter a number between 1 and 20:"))
            elif guess_number<random_number:
                print("higer")
                guess_number=int(input("enter a number between 1 and 20:"))
        else:
            print("the true number was", random_number )
            play_again=input("if you want to play again type yes:")
            while play_again!="yes":
                random_number=random.randint(1,20)
                guess_number=int(input("enter a number between 1 and 20:"))
                counter=2
                while counter>0:
                    if guess_number==random_number:
                        print("correct")
                        break
                    else:
                        if counter!=1:
                            if guess_number>random_number:
                                print("lower")
                                guess_number=int(input("enter a number between 1 and 20:"))
                                counter-=1
                            elif guess_number<random_number:
                                print("higer")
                                guess_number=int(input("enter a number between 1 and 20:"))
                                counter-=1
                        else:
                            print("the true number was", random_number )
                            play_again=input("if you want to play again type yes:")
                            break
                        if  play_again!="yes":
                            print("thank you for playing")
                            break