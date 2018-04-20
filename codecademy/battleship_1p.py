from random import randint


def number_input(message):
    try:
        return int(input(message))
    except ValueError:
        return number_input(message)

debugMode = 0
hintMode = 1
limit = 4
boardSize = 5
board = []


# setting game
boardSize = number_input("Board Size: ")
limit = number_input("Turn Limit: ")

if number_input("Default Mode? (1:Yes, 0:No): ") == 1:
    debugMode = 0
    hintMode = 1
else:
    hintMode = number_input("Hint Mode? (1:Yes, 0:No): ")
    debugMode = number_input("Debug Mode? (1:Yes, 0:No): ")

for x in range(boardSize):
    board.append(["O"] * boardSize)


def getBoardPanel(board):
    tBoard = []
    colList = []
    colBar = []

    for i in range(len(board) + 2):
        if i < 2:
            colList.append(" ")
            colBar.append(" ")
        else:
            colList.append(str(i - 2))
            colBar.append("-")

    for i in range(len(board) + 2):
        if i == 0:
            tBoard.append(colList)
        elif i == 1:
            tBoard.append(colBar)
        else:
            tBoard.append([str(i - 2)] + ["|"] + board[i - 2])

    return tBoard



def print_board(board):
    for row in getBoardPanel(board):
        print(" ".join(row))


print("Let's play Battleship!")


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

if (debugMode == 1):
    print(ship_row)
    print(ship_col)


def endGame(board):
    board[ship_row][ship_col] = "*"
    print_board(board)


def isNearBy(row,col):
    if (row - 1 <= ship_row and ship_row <= row + 1) and (col - 1 <= ship_col and ship_col <= col + 1):
        return True
    else:
        return False



# 이 아래 부분은 전부 다 for 반복문 안에 들어가야 합니다!
# 각 줄마다 네 칸씩 들여쓰기 해야하는 것, 잊지마세요!
turn = 0
while turn < limit:
    print("<< turn: " + str(turn + 1) + " >>")
    print_board(board)

    guess_row = int(number_input("Guess Row:"))
    guess_col = int(number_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        endGame(board)
        break
    else:
        if (guess_row < 0 or guess_row >= boardSize) or (guess_col < 0 or guess_col >= boardSize):
            print("Oops, that's not even in the ocean.")
            turn -= 1
        elif(hintMode == 1 and isNearBy(guess_row, guess_col)):
            print("You missed my battleship, but it is near!")
            board[guess_row][guess_col] = "N"
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
            turn -= 1
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

        if turn == limit - 1:
            print("Game Over")
            endGame(board)

    turn += 1

# End
