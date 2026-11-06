from random import randrange

simboloJuga = "O"
simboloMaqui = "X"

def display_board(board):
    print("-------- EL GATO --------")
    print("JUGADOR (O) VS MAQUINA (X)")
    print("+-----------------------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[1], board[2], board[3]))
    print("|       |       |       |")
    print("|-----------------------|")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[4], board[5], board[6]))
    print("|       |       |       |")
    print("|-----------------------|")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[7], board[8], board[9]))
    print("|       |       |       |")
    print("+-----------------------+")

def enter_move(board):
    movimientoJugador = int(input("ingresa tu movimiento: "))
    board[movimientoJugador] = simboloJuga
    display_board(board)
    
def make_list_of_free_fields(board):
    libres = []
    for i in range(1, 10):
        if board[i] != "X" and board[i] != "O":
            libres.append(i)
    return libres

def victory_for(board, sign):
    if board[1] == board[2] == board[3] == sign: return True
    if board[4] == board[5] == board[6] == sign: return True
    if board[7] == board[8] == board[9] == sign: return True

    if board[1] == board[4] == board[7] == sign: return True
    if board[2] == board[5] == board[8] == sign: return True
    if board[3] == board[6] == board[9] == sign: return True

    if board[1] == board[5] == board[9] == sign: return True
    if board[3] == board[5] == board[7] == sign: return True

    return False

def draw_move(board):
    movimientosLibres = make_list_of_free_fields(board)

    if len(movimientosLibres) > 0:
        movimiento = movimientosLibres[randrange(len(movimientosLibres))]
        board[movimiento] = simboloMaqui
    else:
        print("No hay movimientos disponibles")

def jugar():
    board = ["#",1, 2, 3, 4, "X", 6, 7, 8, 9]
    
    while True:
        display_board(board)
        
        enter_move(board)
        if victory_for(board, simboloJuga):
            print("Ganaste")
            break
            
        draw_move(board)
        if victory_for(board, simboloMaqui):
            display_board(board)
            print("La maquina ha ganado")
            break
            
        if len(make_list_of_free_fields(board)) == 0:
            display_board(board)
            print("Empate")
            break

jugar()