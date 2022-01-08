from numpy import array

# Game class - handles all details regarding instantiation & gameplay
class Game:
    def __init__(self, r, c, p, p1, p2):
        self.r = r
        self.c = c
        self.p = p

        self.board = array([["-1" for i in range(c)] for j in range(r)])
        self.colIndices = [-1 for i in range(c)]
        self.currentPlayer = 1
        self.totalMoves = 0

        self.playerDict = {1: p1, 2: p2}
        self.winStrings = [self.playerDict[1] * self.p, self.playerDict[2] * self.p]
        self.winner = 0

    # destructor
    def __del__(self):
        print("Deleting game instance...")

    # Draws board on screen
    def drawBoard(self):
        for i in range(self.r):
            for j in range(self.c):
                print(self.board[i][j], end=" | ")
            print()
            print("-" * (5 * self.c))

    # Handles moves and player turns
    # return False for any invalid move
    # return -1 for ongoing game and 0 for game over
    def move(self, column):
        try:
            column = int(column)
        except:
            print(f"Please enter a numeric value between 1 - {self.c}")
            return False, -1

        if not 1 <= column <= self.c:
            print(f"Please enter a numeric value between 1 - {self.c}")
            return False, -1

        column = column - 1
        row = self.colIndices[column] + 1

        if row == self.r:
            print(f"Column full, cannot place your move there...")
            return False, -1

        self.totalMoves += 1
        self.board[self.r - 1 - row][column] = self.playerDict[self.currentPlayer]
        self.colIndices[column] += 1

        self.drawBoard()
        self.winner = self.checkWin()
        self.currentPlayer = 1 if self.currentPlayer == 2 else 2

        if self.r * self.c == self.totalMoves:
            print("Game draw...")
            return True, 0

        return True, -1 if self.winner == 0 else 0

    # checks for win after every move for current player
    def checkWin(self):

        winStrings = [self.playerDict[1] * self.p, self.playerDict[2] * self.p]

        # horizontal check
        for i in range(self.r):
            s = "".join(self.board[i])

            if winStrings[self.currentPlayer - 1] in s:
                print(f"Player {self.currentPlayer} won!!!")
                return self.currentPlayer

        # vertical check
        for i in range(self.c):
            s = "".join(self.board[:, i])

            if winStrings[self.currentPlayer - 1] in s:
                print(f"Player {self.currentPlayer} won!!!")
                return self.currentPlayer

        # diagonal check

        # CASE 1 - left bottom to top right
        dx = -1
        dy = 1
        count = 0
        for i in range(self.c - self.p + 1):
            x = self.r - 1
            y = i

            while x >= 0 and y < self.c:

                if self.board[x, y] == self.playerDict[self.currentPlayer]:
                    count += 1
                else:
                    count = 0
                if count == self.p:
                    print(f"Player {self.currentPlayer} won!!!")
                    return self.currentPlayer
                x += dx
                y += dy

        # CASE 2 - right bottom to top left
        dx = -1
        dy = -1
        count = 0
        for i in range(self.c - self.p + 1):
            x = self.r - 1
            y = self.c - i - 1
            print("=========")
            while x >= 0 and y >= 0:
                print(
                    x, y, self.board[x, y], count, self.playerDict[self.currentPlayer]
                )
                if self.board[x, y] == self.playerDict[self.currentPlayer]:
                    count += 1
                else:
                    count = 0
                if count == self.p:
                    print(f"Player {self.currentPlayer} won!!!")
                    return self.currentPlayer
                x += dx
                y += dy

        # CASE 3 - top left to bottom right
        dx = 1
        dy = 1
        count = 0
        for i in range(self.c - self.p + 1):
            x = 0
            y = i

            while x < self.r and y < self.c:

                if self.board[x, y] == self.playerDict[self.currentPlayer]:
                    count += 1
                else:
                    count = 0
                if count == self.p:
                    print(f"Player {self.currentPlayer} won!!!")
                    return self.currentPlayer
                x += dx
                y += dy

        # CASE 4 - top right to bottom left
        dx = 1
        dy = -1
        count = 0
        for i in range(self.c - self.p + 1):
            x = 0
            y = self.c - i - 1

            while x < self.r and y <= 0:

                if self.board[x, y] == self.playerDict[self.currentPlayer]:
                    count += 1
                else:
                    count = 0
                if count == self.p:
                    print(f"Player {self.currentPlayer} won!!!")
                    return self.currentPlayer
                x += dx
                y += dy

        return 0
