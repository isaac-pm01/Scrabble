import numpy as np
import random

# Diccionario de palabras válidas
dictionary = [
    "PISTA", "HASTA", "PAN", "BUSCO", "PISTAS",
    "PISTACHO", "APIO", "COPAS", "COPA", "TE",
    "AL", "TELA", "TESAR", "AHORRO"
]

# Clase para gestionar el tablero
class Board:
    def __init__(self, size=15):
        self.size = size
        self.board = np.full((size, size), "0")  # Usamos "0" para indicar espacios vacíos

    def place_word(self, coord, orientation, word):
        x, y = coord
        word_length = len(word)

        if orientation == "h":
            if y + word_length > self.size:  # Verificar si la palabra sale del borde
                return False
            for i in range(word_length):
                if self.board[x, y + i] != "0" and self.board[x, y + i] != word[i]:
                    return False  # Colisión con otra letra
            for i in range(word_length):
                self.board[x, y + i] = word[i]  # Colocar la palabra
        else:  # vertical
            if x + word_length > self.size:  # Verificar si la palabra sale del borde
                return False
            for i in range(word_length):
                if self.board[x + i, y] != "0" and self.board[x + i, y] != word[i]:
                    return False  # Colisión con otra letra
            for i in range(word_length):
                self.board[x + i, y] = word[i]  # Colocar la palabra
        return True

    def remove_word(self, coord, orientation, word):
        x, y = coord
        word_length = len(word)

        if orientation == "h":
            for i in range(word_length):
                self.board[x, y + i] = "0"  # Vaciar el espacio
        else:  # vertical
            for i in range(word_length):
                self.board[x + i, y] = "0"  # Vaciar el espacio

    def print_board(self):
        for row in self.board:
            print(" ".join(row).replace("0", "-"))


# Clase para gestionar las letras y la bolsa
class LetterBag:
    def __init__(self):
        self.letters = self.initialize_letters()

    def initialize_letters(self):
        # Inicializar la bolsa de letras con 100 fichas según la distribución del Scrabble
        return (
            ["A"] * 9 + ["B"] * 2 + ["C"] * 2 + ["D"] * 4 +
            ["E"] * 12 + ["F"] * 2 + ["G"] * 3 + ["H"] * 2 +
            ["I"] * 9 + ["J"] * 1 + ["K"] * 1 + ["L"] * 4 +
            ["M"] * 2 + ["N"] * 6 + ["O"] * 8 + ["P"] * 2 +
            ["Q"] * 1 + ["R"] * 6 + ["S"] * 4 + ["T"] * 6 +
            ["U"] * 4 + ["V"] * 2 + ["W"] * 2 + ["X"] * 1 +
            ["Y"] * 2 + ["Z"] * 1 + ["_"] * 2  # Comodines
        )

    def draw_letters(self, count):
        if count > len(self.letters):
            count = len(self.letters)
        drawn_letters = random.sample(self.letters, count)
        for letter in drawn_letters:
            self.letters.remove(letter)
        return drawn_letters

    def remaining_letters(self):
        return len(self.letters)


# Clase para la IA
class ScrabbleAI:
    def __init__(self):
        self.used_words = set()  # Almacena las palabras ya jugadas

    def best_move(self, board):
        # Intentar colocar una palabra que aún no se haya usado
        for word in dictionary:
            if word not in self.used_words:
                for x in range(board.size):
                    for y in range(board.size):
                        for orientation in ['h', 'v']:
                            if board.place_word((x, y), orientation, word):
                                # Añadir la palabra al conjunto de usadas y retornar el movimiento
                                self.used_words.add(word)
                                return (word, (x, y), orientation)
        return None  # Pasar el turno si no hay movimientos válidos


# Clase principal para gestionar el juego
class ScrabbleGame:
    def __init__(self):
        self.board = Board()
        self.bag = LetterBag()
        self.players = []
        self.current_player_index = 0
        self.ai = ScrabbleAI()

    def add_player(self, player_name):
        self.players.append(player_name)

    def play_turn(self):
        print(f"\nTurno de {self.players[self.current_player_index]}")
        if self.players[self.current_player_index] == "IA":
            best_move = self.ai.best_move(self.board)
            if best_move:
                word, coord, orientation = best_move
                self.board.place_word(coord, orientation, word)
                print(f"La IA coloca la palabra '{word}' en {coord} ({orientation})")
            else:
                print("La IA pasa su turno.")
        else:
            self.human_turn()

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def human_turn(self):
        while True:
            word = input("Ingrese la palabra: ").upper()
            if word not in dictionary:
                print("Palabra no válida. Intente de nuevo.")
                continue

            coord = input("Ingrese la coordenada (fila,columna): ")
            try:
                x, y = map(int, coord.split(','))
                orientation = input("Ingrese la orientación (h/v): ").lower()
                if orientation not in ['h', 'v']:
                    print("Orientación no válida. Intente de nuevo.")
                    continue

                if self.board.place_word((x, y), orientation, word):
                    print(f"{self.players[self.current_player_index]} coloca la palabra '{word}' en ({x}, {y}) {orientation}.")
                    break
                else:
                    print("No se puede colocar la palabra. Intente de nuevo.")
            except Exception as e:
                print(f"Error en la entrada: {e}. Intente de nuevo.")

    def check_game_over(self):
        if self.bag.remaining_letters() == 0 or len(self.ai.used_words) == len(dictionary):
            print("No quedan más letras en la bolsa o se usaron todas las palabras. Fin del juego.")
            return True
        return False

# Ejemplo de uso
if __name__ == "__main__":
    game = ScrabbleGame()
    game.add_player("Jugador 1")
    game.add_player("IA")
    game.board.print_board()

    while True:
        game.play_turn()
        game.board.print_board()
        if game.check_game_over():
            break







