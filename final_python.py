import random #מייבא את המודול רנדום בשביל בחירות אקראיות
board=[[0,0,0], # הלוח עליו נשחק
       [0,0,0],
       [0,0,0]]
def who_is_one(): #מגדיר מי מתחיל ראשון
    rand_computer=random.choice(["x","o"])
    if rand_computer=="x":
        print("you are 'o',and computer is 'x'")
        user_choice="o"
    elif rand_computer=="o":
        print("you are 'x',and computer is 'o'")
        user_choice="x"
    return rand_computer, user_choice

def win_condison(board): #פונקציה שמקבלת את הלוח ובודקת אם יש מנצח ע"פ אפשרויות הניצחון
    list1=[[[0,0],[0,1],[0,2]],
    [[1,0],[1,1],[1,2]],
    [[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],
    [[0,1],[1,1],[2,1]],
    [[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],
    [[0,2],[1,1],[0,2]]]
    
    for option_wins in list1: #לולאה בתוך לולאה שבודקת כל אפשרות ניצחון
        count_x=0
        count_o=0
        for one_option in option_wins:
            i=one_option[0]
            j=one_option[1]
            if board[i][j]=='x':
                count_x+=1
            if board[i][j]=='o':
                count_o+=1
        if count_x==3:
            return "x win"
        if count_o==3:
            return "o win"
    return None

random_compuster,user_choice=who_is_one()#ייבוא את מי שהמחשב בחר ואת מי שהמשתמש בחר
check=win_condison(board)
while check==None:#לולאה שרצה כל עוד אין מנצח
    for x in range(len(board)):
            print(board[x])
    place_to_put=[]
    place_to_put=input("enter your place you want to put with two numbers splits with ','").split(",")
    row=int(place_to_put[0])
    col=int(place_to_put[1])
    random_place=[random.choice([0,1,2]),random.choice([0,1,2])]
    while board[random_place[0]][random_place[1]]==0 and board[row][col]==0 :
        board[random_place[0]][random_place[1]]=random_compuster
        board[row][col]=user_choice
        check=win_condison(board)
print(f"{check}!")#מדפיס מי ניצח


# def get_player_input(board, player):

#     row = int(input("choose row (0-2): "))
#     col = int(input("choose col (0-2): "))

#     # בדיקה: האם התא תפוס
#     if board[row][col] == "x" or board[row][col] == "o":
#         print("this cell is already choosen , choose different cell")
#         return get_player_input(board, player)   # מבקש שוב מהמשתמש

#     # אם התא פנוי – הכנס את המהלך
#     board[row][col] = player
#     return row, col







