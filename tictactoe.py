import random


class TicTac:
    def __init__(self):
        self.map = [13, 23, 33, 12, 22, 32, 11, 21, 31]
        self.cells = list(" " * 9)

    def output(self):
        cells = self.cells
        lines = "---------"
        output1 = f'{lines}\n' \
                  f'| {cells[0]} {cells[1]} {cells[2]} |\n' \
                  f'| {cells[3]} {cells[4]} {cells[5]} |\n' \
                  f'| {cells[6]} {cells[7]} {cells[8]} |\n' \
                  f'{lines}'
        return output1

    def check(self):
        if self.row_win() is not None:  # is not None
            return self.row_win()
        elif self.col_win() is not None:
            return self.col_win()
        elif self.dia_win() is not None:
            return self.dia_win()
        else:
            if "_" in self.cells or " " in self.cells:
                return None
            else:
                return "Draw"

    def row_win(self):
        for number in [0, 3, 6]:
            if self.cells[number] == self.cells[number + 1] == self.cells[number + 2]:
                if "X" in self.cells[number]:
                    return "X wins"
                elif "O" in self.cells[number]:
                    return "O wins"
            else:
                pass
        return None

    def col_win(self):
        for number in [0, 1, 2]:
            if self.cells[number] == self.cells[number + 3] == self.cells[number + 6]:
                if "X" in self.cells[number]:
                    return "X wins"
                elif "O" in self.cells[number]:
                    return "O wins"
            else:
                pass
        return None

    def dia_win(self):
        if self.cells[0] == self.cells[4] == self.cells[8] or self.cells[2] == self.cells[4] == self.cells[6]:
            if "X" in self.cells[4]:
                return "X wins"
            elif "O" in self.cells[4]:
                return "O wins"
        else:
            return None


class AlmostWin(TicTac):
    def __init__(self, cells):
        super().__init__()
        self.cells = cells

    def row_win_check(self):
        cells = self.cells
        count = 0
        for i in range(3):
            for j in range(2):
                if count in [0, 3, 6] and cells[count] == cells[count+2] and "_" in cells[count+1]:
                    player = cells[count]
                    return player, str(count+1)
                if cells[count] == cells[count + 1]:
                    if count in [0, 3, 6] and " " in cells[count + 2]:
                        player = cells[count]
                        if player != " ":
                            return player, str(count + 2)
                    elif count in [1, 4, 7] and " " in cells[count - 2]:
                        player = cells[count]
                        if player != " ":
                            return player, str(count - 2)
                count += 1
            count += 1

    def col_win_check(self):
        cells = self.cells
        count = 0
        for i in range(3):
            for j in range(2):
                if count in [0, 1, 2] and cells[count] == cells[count+6] and "_" in cells[count+3]:
                    player = cells[count]
                    return player, str(count+3)
                if cells[count] == cells[count + 3]:
                    if count in [0, 1, 2] and " " in cells[count+6]:
                        player = cells[count]
                        if player != " ":
                            return player, str(count+6)
                    elif count in [3, 4, 5] and " " in cells[count-3]:
                        player = cells[count]
                        if player != " ":
                            return player, str(count-3)
                    else:
                        pass
                count += 3
            count = i

    def dia_win_check(self):
        cells = self.cells
        count = 0
        for i in range(2):
            if count == 0 and cells[count] == cells[count + 8] and " " in cells[count + 4]:
                player = cells[count]
                return player, str(count + 4)
            if cells[count] == cells[count+4]:
                if count == 0 and " " in cells[count+8]:
                    player = cells[count]
                    if player != " ":
                        return player, str(count+8)
                elif count == 4 and " " in cells[count-4]:
                    player = cells[count]
                    if player != " ":
                        return player, str(count-4)

            count += 4
        count = 2
        for i in range(2):
            if count == 2 and cells[count] == cells[count + 4] and " " in cells[count + 2]:
                player = cells[count]
                return player, str(count + 2)
            if cells[count] == cells[count + 2]:
                if count == 2 and " " in cells[count+4]:
                    player = cells[count]
                    if player != " ":
                        return player, str(count+4)
                elif count == 4 and " " in cells[count-2]:
                    player = cells[count]
                    if player != " ":
                        return player, str(count-2)
            count += 2


class MaxMin(TicTac):
    def __init__(self, player, cells):
        super().__init__()
        if player == "X":
            self.player = player
            self.player2 = "O"
        else:
            self.player = player
            self.player2 = "X"
        self.score = 0
        self.cells = cells

    def bestmove(self):
        best_score = -1000
        move = 0        # This will get us the index where we will place our final player
        count = 0       # This is so that we can find exact index to place our temp player
        for position in self.cells:
            if position == " ":
                self.cells[count] = self.player
                self.score = self.minimax(0, False)
                self.cells[count] = " "
                if self.score > best_score:
                    best_score = self.score
                    move = count
            count += 1
        return move

    def minimax(self, depth, is_maximizing):
        result = self.check()
        score = 0
        if result is not None:
            if result == "X wins":
                if self.player == "X":
                    score = +1
                else:
                    score = -1
            elif result == "O wins":
                if self.player == "O":
                    score = +1
                else:
                    score = -1
            elif result == "Draw":
                score = 0
            return score
        if is_maximizing:
            best_score = -1000
            count = 0
            for position in self.cells:
                if position == " ":
                    self.cells[count] = self.player
                    score += self.minimax(depth + 1, False)
                    self.cells[count] = " "
                    best_score = max(score, best_score)
                count += 1
            return best_score
        else:
            best_score = 1000
            count = 0
            for position in self.cells:
                if position == " ":
                    self.cells[count] = self.player2
                    score += self.minimax(depth + 1, True)
                    self.cells[count] = " "
                    best_score = min(score, best_score)
                count += 1
            return best_score


class Moves(TicTac):
    def __init__(self):
        super().__init__()

    def ai_easy(self, player):
        while True:
            next_move = random.choice(self.map)
            index = self.map.index(next_move)
            if self.cells[index] == " ":
                print('Making move level "easy"')
                self.cells[index] = player
                break
            else:
                continue
        return self.output()

    def ai_medium(self, player):
        print('Making move level "medium"')
        check = AlmostWin(self.cells)
        wins1 = check.row_win_check()
        wins2 = check.dia_win_check()
        wins3 = check.col_win_check()
        wins = None
        if wins1 is not None and wins1[0] != " ":
            wins = wins1
        elif wins2 is not None and wins2[0] != " ":
            wins = wins2
        elif wins3 is not None and wins3[0] != " ":
            wins = wins3
        else:
            while True:
                next_move = random.choice(self.map)
                index = self.map.index(next_move)
                if self.cells[index] == " ":
                    self.cells[index] = player
                    break
                else:
                    continue
            return self.output()
        self.cells[int(wins[1])] = player
        return self.output()

    def ai_hard(self, player):
        print('Making move level "hard"')
        if "O" not in self.cells and "X" not in self.cells:
            while True:
                next_move = random.choice(self.map)
                index = self.map.index(next_move)
                if self.cells[index] == " ":
                    self.cells[index] = player
                    break
                else:
                    continue
            return self.output()
        best = MaxMin(player, self.cells)
        index = best.bestmove()
        self.cells[index] = player
        return self.output()

    def input(self, player):
        while True:
            next_move = input("Enter the coordinates: ")
            next_move = next_move.replace(" ", "")
            if next_move[0] in ["1", "2", "3"] and next_move[1] in ["1", "2", "3"]:
                next_move = int(next_move)
                index = self.map.index(next_move)
                if self.cells[index] == " ":
                    self.cells[index] = player
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif not next_move.isdigit():
                print("You should enter numbers!")
                continue
            else:
                print("Coordinates should be from 1 to 3!")
                continue
            return self.output()


class Engine(Moves):
    def __init__(self):
        super().__init__()
        self.player_one = None
        self.player_two = None

    def players(self):
        command_list = ["start", "exit", "user", "easy", "medium", "hard"]
        while True:
            self.cells = list(" " * 9)
            parameter = input("Input command: ")
            parameter = parameter.split(' ')
            if parameter[0].lower() == "start":
                if len(parameter) < 3:
                    print("Bad parameters!")
                    continue
                if parameter[1] == "user":
                    self.player_one = "user"
                elif parameter[1] == "easy":
                    self.player_one = "easy"
                elif parameter[1] == "medium":
                    self.player_one = "medium"
                elif parameter[1] == "hard":
                    self.player_one = "hard"
                else:
                    print("Bad parameters!")
                    continue
                if parameter[2] == "user":
                    self.player_two = "user"
                elif parameter[2] == "easy":
                    self.player_two = "easy"
                elif parameter[2] == "medium":
                    self.player_two = "medium"
                elif parameter[2] == "hard":
                    self.player_two = "hard"
                else:
                    print("Bad parameters!")
                    continue
            elif parameter[0].lower() == "exit":
                exit(0)
            else:
                print("Bad parameters!")
                continue
            print(self.play())

    def play(self):
        print(self.output())
        while True:
            if self.player_one == "user":
                print(self.input("X"))
            elif self.player_one == "easy":
                print(self.ai_easy("X"))
            elif self.player_one == "medium":
                print(self.ai_medium("X"))
            elif self.player_one == "hard":
                print(self.ai_hard("X"))
            if self.check() is not None:
                return self.check()
            else:
                pass
            if self.player_two == "user":
                print(self.input("O"))
            elif self.player_two == "easy":
                print(self.ai_easy("O"))
            elif self.player_two == "medium":
                print(self.ai_medium("O"))
            elif self.player_two == "hard":
                print(self.ai_hard("O"))
            if self.check() is not None:
                return self.check()
            else:
                pass


if __name__ == "__main__":
    toe = Engine()
    toe.players()
