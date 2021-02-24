import numpy as np
import random
import os
import constants


class Radar:
    """ Set... """

    def __init__(self, rows=constants.ROWS, columns=constants.COLUMNS):
        self.board = np.empty((rows, columns), dtype=str)
        self.board[:] = '≈'

    def view_board(self, rows=constants.ROWS, columns=constants.COLUMNS):
        print('+\t' * columns)
        print()
        for i in range(columns):
            for j in range(rows):
                print(self.board[j][i] + '\t', end="")
            print()
        print()


class Board(Radar):
    """ Represent and manipulate the board of the player"""

    def __init__(self, rows=constants.ROWS, columns=constants.COLUMNS):
        super(Board, self).__init__(rows=constants.ROWS, columns=constants.COLUMNS)

    def valid_coordinates(self, x, y):
        """ Check if the given coordinates are valid. Return True if x and y are valid, False otherwise. """
        try:
            self.board[y][x]
            return True
        except IndexError:
            return False

    def available_col(self, x, y, size):
        for i in range(size):
            if self.valid_coordinates(x, y) and self.board[y][x] == '≈':
                x += 1
            else:
                return False
        return True

    def available_row(self, x, y, size):
        for i in range(size):
            if self.valid_coordinates(x, y) and self.board[y][x] == '≈':
                y += 1
            else:
                return False
        return True

    def set_vertical_ship(self, x, y, size):
        for i in range(size):
            self.board[y][x] = '#'
            x += 1

    def set_horizontal_ship(self, x, y, size):
        for i in range(size):
            self.board[y][x] = '#'
            y += 1


class Ship():

    def __init__(self, size):
        self.size = size
        self.coordinates = []

    def coords_vertical(self, x, y):
        for i in range(self.size):
            self.coordinates.append((x, y))
            x += 1

    def coords_horizontal(self, x, y):
        for i in range(self.size):
            self.coordinates.append((x, y))
            y += 1

    def status(self):
        if not self.coordinates:
            return True
        else:
            return False


class Player:

    def __init__(self, name):
        self.name = name
        self.radar = Radar()
        self.board = Board()
        self.fleet = []

    def set_fleet(self):

        for ship in constants.SHIPS:

            while True:
                x = random.randint(0, constants.COLUMNS - 1)
                y = random.randint(0, constants.ROWS - 1)

                orientation = random.choice(constants.ORIENTATION)

                if orientation == 'V' and self.board.available_col(x, y, ship):
                    self.board.set_vertical_ship(x, y, ship)
                    my_ship = Ship(ship)
                    my_ship.coords_vertical(x, y)
                    self.fleet.append(my_ship)
                    break
                elif orientation == 'H' and self.board.available_row(x, y, ship):
                    self.board.set_horizontal_ship(x, y, ship)
                    my_ship = Ship(ship)
                    my_ship.coords_horizontal(x, y)
                    self.fleet.append(my_ship)
                    break

    def print_console(self):
        print("Board")
        self.board.view_board()
        print("Radar")
        self.radar.view_board()

    def save_hit(self, x, y):
        for ship in self.fleet:
            if (x, y) in ship.coordinates:
                ship.coordinates.remove((x, y))
                if ship.status():
                    self.fleet.remove(ship)

    def attack(self, target):
        self.print_console()
        try:
            x = int(input("x coord: "))
            y = int(input("y coord: "))

            if self.board.valid_coordinates(x, y):
                if target.board.board[y][x] == '#':
                    target.board.board[y][x] = 'X'
                    target.save_hit(x, y)
                    self.radar.board[y][x] = 'X'
                elif self.radar.board[y][x] == '*' or self.radar.board[y][x] == 'X':
                    print("This point was already hitted!")
                    self.attack(target)
                else:
                    self.radar.board[y][x] = '*'
                    target.board.board[y][x] = '*'
            else:
                print("Out of range!")
                self.attack(target)
        except ValueError:
            print("Only integers are allowed")
            self.attack(target)
        input('Press enter.')
        os.system('clear')


class Computer(Player):
    def __init__(self):
        super(Computer, self).__init__(self)
        self.name = 'Computer'

    def attack(self, target):
        x = random.randint(0, constants.COLUMNS - 1)
        y = random.randint(0, constants.ROWS - 1)

        if target.board.board[y][x] == '#':
            target.board.board[y][x] = 'X'
            target.save_hit(x, y)
            self.radar.board[y][x] = 'X'
        elif self.radar.board[y][x] == '*' or self.radar.board[y][x] == 'X':
            print("This point was already hitted!")
            self.attack(target)
        else:
            self.radar.board[y][x] = '*'
            target.board.board[y][x] = '*'


class Battleship:

    def __init__(self):
        self.result = True
        self.play()

    def clear_console(self):
        os.system('clear')

    def fleet_beated(self, player):
        return player.fleet == []

    def play(self):
        player = Player(input("Write your name: "))
        player.set_fleet()
        player.print_console()
        input("Press Enter")
        self.clear_console()

        computer = Computer()
        computer.set_fleet()
        self.clear_console()

        while True:
            player.attack(computer)
            if self.fleet_beated(computer):
                break
            else:
                self.clear_console()
                computer.attack(player)
                if self.fleet_beated(player):
                    self.result = False
                    break