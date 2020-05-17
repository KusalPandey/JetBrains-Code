cells = ["_","_","_","_","_","_","_","_","_"]
index = None
location = [13, 23, 33, 12, 22, 32, 11, 21, 31]
x_count = 2
o_count = 1

print("---------")
print("|", cells[0], cells[1], cells[2], "|")
print("|", cells[3], cells[4], cells[5], "|")
print("|", cells[6], cells[7], cells[8], "|")
print("---------")

while "_" in cells:
    next_move = input("Enter the coordinates: ")
    next_move = next_move.replace(" ", "")
    move = list(next_move)
    x, y = move[0], move[1]

    if next_move.isdigit() is False:
        print("You should enter numbers!")
        break
    elif int(x) not in [1, 2, 3] or int(y) not in [1, 2, 3]:
        print("Coordinates should be from 1 to 3!")
        continue

    for number in range(9):
        if int(next_move) == location[number]:
            index = number

    if "X" in cells[index] or "O" in cells[index]:
        print("This cell is occupied! choose another one!")
        continue

    if x_count % 2 == 0:
        cells[index] = "X"
        x_count = x_count + 1
        o_count = o_count + 1

    elif o_count % 2 == 0:
        cells[index] = "O"
        x_count = x_count + 1
        o_count = o_count + 1

    print("---------")
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print("---------")


def check():
    winner = []
    row_win = False
    col_win = False
    dia_win = False
    global x_count
    global o_count

    for number in [0, 3, 6]:
        if cells[number] == cells[number + 1] == cells[number + 2]:
            row_win = True
            if "X" in cells[number]:
                winner.append("X")

            if "O" in cells[number]:
                winner.append("Y")
        else:
            row_win = False

    for number in [0, 1, 2]:
        if cells[number] == cells[number + 3] == cells[number + 6]:
            col_win = True
            if "X" in cells[number]:
                winner.append("X")
            if "O" in cells[number]:
                winner.append("Y")
        else:
            col_win = False

    if cells[0] == cells[4] == cells[8] or cells[2] == cells[4] == cells[6]:
        dia_win = True
        if "X" in cells[4]:
            winner.append("X")
        if "O" in cells[4]:
            winner.append("Y")
    else:
        dia_win = False

    difference = x_count - o_count

    if abs(difference) >= 2:
        print("Impossible")
    else:
        if (row_win is True and col_win is True) or ("X" in winner and "Y" in winner):
            print("Impossible")
        else:
            if "X" in winner:
                print("X wins")
            elif "Y" in winner:
                print("O wins")
            elif "_" in cells or " " in cells:
                print("Game not finished")
            elif row_win is False and col_win is False:
                print("Draw")


check()
