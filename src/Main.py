from utils import Battleship


def start_game():
    print("Welcome to the game")
    print("Instructions")
    print(""""

        How to Play the Battleship Board Game?
        In this game you are going to play against the computer
        If you want to play you should write 'yes' to go ahead once the program has started.
        You have to introduce your username to play.
        to attempt to hit the opponent's enemy ships, the coordinates of the locations must be entered as:
        "coor x: and coor y" expression
        So On your turn, call out x,y coordinats that identifies a row and column on your target grid.
        The coordinates must be integers between 0 and 9.
        The winner is the one that take down the opponent's fleet.
        Each fleet is composed of 10 ships of 4 different types.

    """)
start = ''
while start != 'yes' and start != 'no':
    start = input("Play? (yes/no) ")

    if start.lower() == 'yes':
        battle = Battleship()
        if battle.result:
            print("You won")
        else:
            print("The computer won")
    elif start.lower() == 'no':
        print('Goodbye!')
    else:
        print('Wrong answer, try again ;)')

if __name__ == "__main__":
    start_game()
