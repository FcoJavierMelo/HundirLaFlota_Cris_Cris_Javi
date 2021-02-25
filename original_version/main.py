import library as lib


tablero_jugador = lib.crearTablero()
lib.inicializarBarcos(tablero_jugador)

tablero_pc = lib.crearTablero()
lib.inicializarBarcos(tablero_pc)

tablero_disparos_jugador = lib.crearTablero()
tablero_disparos_pc = lib.crearTablero()

acierto_usuario = True
acierto_maquina = True
gana_usuario = False
gana_pc = False


#while principal -> mientras que ninguno gane
while (gana_usuario == False and gana_pc == False):
    #empieza el usuario
    #si el pc no ha ganado -> yo puedo jugar
    if (gana_pc == False):
        #si he acertado la posicion del barco -> sigo jugando y vuelvo a pedir coordenadas, etc
        #sigo jugando en caso que no haya ganado 
        while (acierto_usuario == True and gana_usuario == False):
            lib.borrarPantalla()
            lib.imprimirJuego(tablero_jugador, tablero_disparos_pc, "TURNO JUGADOR")

            #pedimos coordenadas de la posicion
            coordenada_x = lib.pedirCoordenada("fila")
            coordenada_y = lib.pedirCoordenada("columna")
            
            #repetimos la introducción de coordenadas en caso que estén ocupadas
            while (tablero_disparos_pc[coordenada_x][coordenada_y] == 'O' or tablero_disparos_pc[coordenada_x][coordenada_y] == 'X'):
                print("Posición ya seleccionada")
                coordenada_x = lib.pedirCoordenada("fila")
                coordenada_y = lib.pedirCoordenada("columna")
            
            #comprobamos si el usuario acierta con la posicion
            acierto_usuario = lib.buscarCoordenada(coordenada_x, coordenada_y, tablero_pc, tablero_disparos_pc)
            
            #comprobamos si el usuario gana
            gana_usuario = lib.comprobarBarcos(tablero_disparos_pc)
            
            #si gana el usuario -> mostramos el mensaje
            if (gana_usuario == True):
                    print("¡¡¡¡¡¡HAS GANADO!!!!!!")
    
    #si el jugador no ha ganado -> el pc puede jugar
    if (gana_usuario == False):
        #si falla sigue la maquina
        
        #si la maquina acierta -> sigue jugando
        #sigue jugando siempre que no haya ganado ya
        while (acierto_maquina == True and gana_pc == False):
            lib.borrarPantalla()
            lib.imprimirJuego(tablero_pc, tablero_disparos_jugador, "TURNO MÁQUINA")
            
            input().split(' ')[0]
            
            
            #creamos posicion aleatoria de juego del pc
            coordenada_x = lib.posicionAleatoria()
            coordenada_y = lib.posicionAleatoria()

            #repetimos la introducción de coordenadas en caso que estén ocupadas
            while (tablero_disparos_jugador[coordenada_x][coordenada_y] == 'O' or tablero_disparos_jugador[coordenada_x][coordenada_y] == 'X'):
                coordenada_x = lib.posicionAleatoria()
                coordenada_y = lib.posicionAleatoria()
        
            #comprobamos que la maquina ha acertado con esa posicion aleatoria
            acierto_maquina = lib.buscarCoordenada(coordenada_x, coordenada_y, tablero_jugador, tablero_disparos_jugador)
            
            #comprobamos si ha ganado
            gana_pc = lib.comprobarBarcos(tablero_disparos_jugador)
            
            #si gana el pc mostramos mensaje 
            if (gana_pc == True):
                print("¡¡¡¡¡¡HAS PERDIDO!!!!!!")
        
    acierto_maquina = True
    acierto_usuario = True
