from old_version.Clases import Tablero

tablero_usuario = Tablero()
tablero_maquina = Tablero()

print(tablero_usuario.tablero)
print('')
print('')
print(tablero_maquina.tablero)

lista_barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

tablero_maquina.barcos_maquina(lista_barcos)

print('')
print(tablero_maquina.tablero)

while len(lista_barcos) > 0:
    orientacion = input("Introduzca orientación N,S,E,O")
    eslora = int(input("Introduzca eslora"))
    fila = int(input("Introduzca fila"))
    columna = int(input("Introduzca columna"))

    if eslora in lista_barcos:
        if tablero_usuario.barcos_usuario(orientacion, eslora, fila, columna):
            lista_barcos.pop(lista_barcos.index(eslora))
        else:
            print('No se puede colocar un barco en esta posición')
    else:
        print("No quedan barcos de esta eslora")

    print(tablero_usuario.tablero)

print(tablero_usuario.tablero)
