import random  # מייבא את המודול רנדום בשביל בחירות אקראיות

def tic_tac_toe():  # פונקציית המשחק הראשית

    board = [[0,0,0],  # הלוח עליו נשחק
             [0,0,0],
             [0,0,0]]

    def who_is_one():  # מגדיר מי מתחיל ראשון
        rand_computer = random.choice(["x", "o"])
        if rand_computer == "x":
            print("you are 'o', and computer is 'x'")
            user_choice = "o"
        else:
            print("you are 'x', and computer is 'o'")
            user_choice = "x"
        return rand_computer, user_choice

    def win_condison(board):  # פונקציה שבודקת אם יש מנצח
        list1 = [
            [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
            [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
            [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]
        ]

        for option_wins in list1:
            count_x = 0
            count_o = 0
            for i, j in option_wins:
                if board[i][j] == 'x':
                    count_x += 1
                if board[i][j] == 'o':
                    count_o += 1
            if count_x == 3:
                return "x win"
            if count_o == 3:
                return "o win"
        return None

    def is_draw(board):
        for row in board:
            if 0 in row:
                return False
        return True

    def get_player_input(board):
        while True:
            try:
                row = int(input("enter row (0-2): "))
                col = int(input("enter column (0-2): "))

                if row not in [0,1,2] or col not in [0,1,2]:
                    print("Choose only 0, 1, or 2.")
                    continue

                if board[row][col] != 0:
                    print("That spot is taken.")
                    continue

                return row, col

            except ValueError:
                print("Numbers only!")

    def bot_move(board):
        # ניסיון לנצח
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 'x'
                    if win_condison(board) == "x win":
                        board[i][j] = 0
                        return (i, j)
                    board[i][j] = 0

        # ניסיון לחסום את השחקן
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 'o'
                    if win_condison(board) == "o win":
                        board[i][j] = 0
                        return (i, j)
                    board[i][j] = 0

        # בחירה אקראית אם אין מהלך קריטי
        empty = [(i,j) for i in range(3) for j in range(3) if board[i][j] == 0]
        return random.choice(empty)

    def game_board(board1):  # מדפיס את הלוח יפה
        print("\nBoard:")
        for row in board1:
            print(["_" if x == 0 else x for x in row])
        print()

    first_player, user_choice = who_is_one()  # קובע מי מתחיל ראשון
    game_board(board)

    while True:  # לולאת המשחק הראשית

        if first_player == "x":  # תור המחשב
            print("Computer's turn...")
            bot_pos = bot_move(board)
            board[bot_pos[0]][bot_pos[1]] = 'x'
            game_board(board)

            if win_condison(board) == "x win":
                print("computer win")
                break

            if is_draw(board):
                print("Draw!")
                break

            first_player = "o"

        else:  # תור השחקן
            print("Your turn...")
            player_pos = get_player_input(board)
            board[player_pos[0]][player_pos[1]] = 'o'
            game_board(board)

            if win_condison(board) == "o win":
                print("you win")
                break

            if is_draw(board):
                print("Draw!")
                break

            first_player = "x"

# הפעלת המשחק
tic_tac_toe()

#hello is check and another check with git