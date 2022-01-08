import sys, getopt
from Game import Game

# Function to take necessary details from players


def createGame(r, c, p):

    p1 = input("Player 1 : Select your color from red(r) or yellow(y) : ")
    while p1 not in ["r", "y"]:
        p1 = input("Player 1 : Select a valid color from red(r) or yellow(y) : ")

    p2 = "r" if p1 == "y" else "y"
    print("Player 2 is being assigned color", p2)

    print('Input "exit" to stop playing anytime...')

    # game object instantiation
    game = Game(r, c, p, p1, p2)
    game.drawBoard()

    winner = None

    # loop till one of the player wins
    while not winner:
        col = input(f"Player {game.currentPlayer} : Enter your move - ")
        if col == "exit":
            del game
            exit()

        validMove, gameStatus = game.move(col)
        if gameStatus == 0:
            del game
            restart(r, c, p)

        while not validMove:
            col = input(f"Player {game.currentPlayer} : Enter a valid move - ")
            validMove, gameStatus = game.move(col)


def restart(r, c, p):
    choice = input("Do you want to play again? (Y or N)")
    if choice in ["y", "Y", "YES", "yes", "Yes"]:
        createGame(r, c, p)
    elif choice in ["n", "N", "No", "no", "NO"]:
        exit()
    else:
        restart(r, c, p)


if __name__ == "__main__":

    # handling command-line arguments input

    options = "r:c:p:"
    arguments = sys.argv[1:]

    args, values = getopt.getopt(arguments, options, [])

    r = c = p = None

    try:

        for k, v in args:
            if k == "-r":
                r = int(v)
            elif k == "-c":
                c = int(v)
            elif k == "-p":
                p = int(v)
            else:
                print("Unrecognized option(s) : ", k)
                sys.exit()
        if not p or not r or not c:
            raise Exception(
                "Please define values in run command using -r -c -p option flags..."
            )
        if p > r or p > c:
            raise Exception("p must be in range 1 - maximum(r, c)...")

    except Exception as e:
        print(f"Invalid option(s)...\nTerminating...\n{e}")
        exit()

    createGame(r, c, p)
