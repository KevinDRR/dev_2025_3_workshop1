import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        opciones_validas = ["piedra", "papel", "tijera"]
        j1 = jugador1.lower()
        j2 = jugador2.lower()

        if j1 not in opciones_validas or j2 not in opciones_validas:
            return "invalid"
        
        if j1 == j2:
            return "empate"
        
        if (j1 == "piedra" and j2 == "tijera") or \
           (j1 == "tijera" and j2 == "papel") or \
           (j1 == "papel" and j2 == "piedra"):
            return "jugador1"
        else:
            return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        for fila in tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return fila[0]

        for col in range(3):
            if tablero[0][col] != " " and tablero[0][col] == tablero[1][col] == tablero[2][col]:
                return tablero[0][col]

        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            if all(" " not in fila for fila in tablero):
                return tablero[0][0]

        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            if all(" " not in fila for fila in tablero):
                return tablero[0][2]

        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, fila_inicial, col_inicial, fila_final, col_final, tablero):
        if not (0 <= fila_inicial < 8 and 0 <= col_inicial < 8 and
                0 <= fila_final < 8 and 0 <= col_final < 8):
            return False

        if fila_inicial == fila_final and col_inicial == col_final:
            return False

        if fila_inicial == fila_final:
            paso = 1 if col_final > col_inicial else -1
            for c in range(col_inicial + paso, col_final, paso):
                if tablero[fila_inicial][c] != " ":
                    return False
            return True

        if col_inicial == col_final:
            paso = 1 if fila_final > fila_inicial else -1
            for f in range(fila_inicial + paso, fila_final, paso):
                if tablero[f][col_inicial] != " ":
                    return False
            return True

        return False