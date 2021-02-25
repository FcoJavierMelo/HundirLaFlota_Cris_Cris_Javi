import constants as ct
import numpy as np
import random as rn
import os 

#funcion que crea el tablero de juego
def crearTablero():
    tablero = np.full((ct.DIMENSION, ct.DIMENSION), '≈') 
    return tablero

#funcion que indica si el barco lo ponemos horizontal o vertical
def alineacionBarco():
    alineacion = rn.randint(0, 1)  
    return alineacion

#funcion que devuelve una posicion aleatoria de donde se va a guardar el barco
def posicionAleatoria():
    numero = rn.randint(0, ct.DIMENSION - 1)
    return numero

#funcion que coloca el barco en el tablero aleatoriamente
def colocarBarcoTablero(barco, tablero):
    error = False
    
    x = posicionAleatoria()
    y = posicionAleatoria()
    alineacion = alineacionBarco()
    
    #si alineacion es cero lo coloco en horizontal
    if (alineacion == 0): #horizontal
        #recorrer la lista de la variable barco
        for i in range(0, len(barco)):
            #comprobar si ha habido un error al añadir el barco
            if (error == True):
                #salir del bucle
                break
            else:
                #si no hay error
                #si la posicion y aleatoria + tamaño lista barco es mennor que la dimensión del tablero
                if (y + len(barco) < ct.DIMENSION - 1):
                    #comprobar que ya no exista un barco en esa posicion
                    if (tablero[x][y + i] == '≈'):
                        #si es ≈ ponemos el barco
                        tablero[x][y + i] = barco[i] 
                    else:
                        #asignamos la variable error para que no siga colocando
                        error = True
                else:
                    #marcamos el error a true para indicar que no se puede poner el barco
                    #no tenemos posiciones para poder ponerlo
                    error = True
       
    #si alineacion es uno lo coloco en vertical
    elif (alineacion == 1): #vertical
         #recorrer la lista de la variable barco
        for i in range(0, len(barco)):
            #comprobar si ha habido un error al añadir el barco
            if (error == True):
                #salir del bucle
                break
            else:
                #si no hay error
                #si la posicion x aleatoria + tamaño lista barco es mennor que la dimensión del tablero
                if (x + len(barco) < ct.DIMENSION - 1):
                    #comprobar que ya no exista un barco en esa posicion
                    if (tablero[x + i][y] == '≈'):
                         #si es ≈ ponemos el barco
                        tablero[x + i][y] = barco[i] 
                    else:
                        #asignamos la variable error para que no siga colocando
                        error = True
                else:
                    #marcamos el error a true para indicar que no se puede poner el barco
                    #no tenemos posiciones para poder ponerlo
                    error = True
                    
    return error
    
#funcion que coloca el barco en el tablero 
def colocarBarcos(barco, tablero):
    error = True

    #repetimos el intento de colocar el barco mientras que haya error
    while (error == True):
        error = colocarBarcoTablero(barco, tablero)
    

#funcion que coloca todos los barcos en el tablero
def inicializarBarcos(tablero):
    #colocamos los barcos
    colocarBarcos(ct.BARCO_4, tablero)
    colocarBarcos(ct.BARCO_3, tablero)
    colocarBarcos(ct.BARCO_3, tablero)
    colocarBarcos(ct.BARCO_2, tablero)
    colocarBarcos(ct.BARCO_2, tablero)
    colocarBarcos(ct.BARCO_2, tablero)
    colocarBarcos(ct.BARCO_1, tablero)
    colocarBarcos(ct.BARCO_1, tablero)
    colocarBarcos(ct.BARCO_1, tablero)
    colocarBarcos(ct.BARCO_1, tablero)


#funcion que busca coordenada en el tablero
def buscarCoordenada(x, y, tablero_barcos, tablero_disparos):
    if (tablero_barcos[x][y] == '≈'):
        tablero_disparos[x][y] = 'O'
        return False
    else:
        tablero_disparos[x][y] = 'X'
        return True

def comprobarBarcos(tablero):
    gana = False
    total = 0;
    
    #recorremos el tablero
    for i in range(0, len(tablero)):
        for j in range(0, len(tablero)):
            #si hay una 'X' incrementamos el total
            if (tablero[i][j] == 'X'):
                total = total + 1
    
    #si el total son 20 'X' --> gana
    if (total == 20):
        gana = True
        
    return gana
   
     
def imprimirJuego(tablero_juego, tablero_disparos, mensaje):
        print("--------------" + mensaje + "-----------------")
        print(tablero_juego)
        print()
        print(tablero_disparos)


def pedirCoordenada(coordenada):
    valor_coordenada = input("Introduce coordenada " + coordenada + ": ")

    #comprobamos cadena vacia o con espacios en blanco
    while (valor_coordenada.strip() == ''):
        print("Debe indicarse un valor numérico")
        valor_coordenada = input("Introduce coordenada " + coordenada + ": ")

    #si la cadena ya no es vacía y tiene numero
    #le quitamos una posición
    valor_coordenada = int(valor_coordenada) - 1
    
    #mientras que el valor de la posicion sea menor que cero o mayor que 9
    while (valor_coordenada < 0 or valor_coordenada > 9):
        print("Debe indicarse un valor numérico entre 1 y 10")
        valor_coordenada = input("Introduce coordenada " + coordenada + ": ")
        valor_coordenada = int(valor_coordenada) - 1
        

    return valor_coordenada;

def borrarPantalla(): 
    for i in range(0, 90):
        print()