import numpy as np
import random


class Tablero:
    tablero = np.full((10, 10), '≈')

    def barcos_maquina(self, barcos):
        for i in barcos:
            eslora = i
            while True:
                orient = random.choice(['N', 'S', 'E', 'O'])
                current_pos = np.random.randint(10, size=2)

                fila = current_pos[0]
                col = current_pos[1]

                coord_posi_n = self.tablero[fila:(fila - eslora):-1, col]
                coord_posi_e = self.tablero[fila, col: col + eslora]
                coord_posi_s = self.tablero[fila:(fila + eslora), col]
                coord_posi_o = self.tablero[fila, col: col - eslora:-1]

                if (orient == 'N') and (len(coord_posi_n) == eslora) and ('O' not in coord_posi_n):
                    self.tablero[fila:(fila - eslora):-1, col] = 'O'
                    break
                elif (orient == 'E') and (len(coord_posi_e) == eslora) and ('O' not in coord_posi_e):
                    self.tablero[fila, col: col + eslora] = 'O'
                    break
                elif (orient == 'S') and (len(coord_posi_s) == eslora) and ('O' not in coord_posi_s):
                    self.tablero[fila:(fila + eslora), col] = 'O'
                    break
                elif (orient == 'O') and (len(coord_posi_o) == eslora) and ('O' not in coord_posi_o):
                    self.tablero[fila, col: col - eslora:-1] = 'O'
                    break

    def barcos_usuario(self, orient, eslora, fila, col):

        coord_posi_n = self.tablero[fila:(fila - eslora):-1, col]
        coord_posi_e = self.tablero[fila, col: col + eslora]
        coord_posi_s = self.tablero[fila:(fila + eslora), col]
        coord_posi_o = self.tablero[fila, col: col - eslora:-1]

        if (orient == 'N') and (len(coord_posi_n) == eslora) and ('O' not in coord_posi_n):
            self.tablero[fila:(fila - eslora):-1, col] = 'O'
            return True
        elif (orient == 'E') and (len(coord_posi_e) == eslora) and ('O' not in coord_posi_e):
            self.tablero[fila, col: col + eslora] = 'O'
            return True
        elif (orient == 'S') and (len(coord_posi_s) == eslora) and ('O' not in coord_posi_s):
            self.tablero[fila:(fila + eslora), col] = 'O'
            return True
        elif (orient == 'O') and (len(coord_posi_o) == eslora) and ('O' not in coord_posi_o):
            self.tablero[fila, col: col - eslora:-1] = 'O'
            return True
        else:
            return False
