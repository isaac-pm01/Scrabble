import numpy as np
import random


dictionary = [
    "ABACATE", "ABANICO", "ABISPA", "ABREVAJOS", "ABRIGO", "ACEITUNA", "ACELGA", "ACIDO", "ACORDE", "ACROBACIA",
"ADAPTAR", "AFICION", "AGUACATE", "AGUARDIENTE", "AGUJERO", "ALBA", "ALBUM", "ALBUMINA", "ALFILER", "ALGA",
"ALMENDRA", "ALMORZAR", "ALONDRA", "ALQUIMIA", "AMAPOLA", "AMISTAD", "ANIMAL", "ANIS", "ANULAR", "ANZUELO",
"APICULTOR", "APRENDER", "ARCO", "AROMA", "ARQUITECTO", "ARTISTA", "ASEO", "ATENEA", "ATISBO", "AVENTURA",
"AVE", "BAILE", "BAJAR", "BALON", "BALSA", "BANANA", "BARCO", "BASTON", "BEBER", "BESAR",
"BICICLETA", "BISABUELO", "BLANCO", "BOCADILLO", "BOLSA", "BOMBA", "BOTELLA", "BRAZO", "BURLA", "CABELLO",
"CADENA", "CAFETERA", "CAJA", "CALAMAR", "CALENTAR", "CALIBRE", "CAMPANA", "CAMPUS", "CANAL", "CANGREJO",
"CANTAR", "CANTINA", "CAPITAN", "CARACOL", "CARNICERO", "CARRERA", "CASA", "CASTILLO", "CEBOLLA", "CELESTE",
"CELULAR", "CENIZAS", "CEREZA", "CETRO", "CHOCOLATE", "CILINDRO", "CINTURA", "CIRCO", "CITA", "CLAVE",
"CLOVER", "COCHE", "CONEJO", "CONTRA", "CORCHO", "CORRAL", "COSAS", "CRUZ", "CUPON", "CURSO",
"DAMA", "DEBER", "DERRUMBE", "DESIERTO", "DIA", "DINERO", "DISCO", "DOCENTE", "DOLOR", "DORMIR",
"DULCE", "EJERCICIO", "ELASTICO", "EMOCION", "ENEMIGO", "ENVIAR", "ERIZO", "ESCALERA", "ESCRITOR", "ESPERANZA",
"ESTA", "ESTADIO", "ESTRELLA", "ETAPA", "EXITO", "FANAL", "FELIZ", "FLORES", "FLUJO", "FORO",
"FRANQUEZA", "FRUTA", "FUNDA", "GAFAS", "GATO", "GEOMETRIA", "GERANIO", "GOL", "GORRA", "GRANDE",
"GRECIA", "GUACAMAYO", "HABITACION", "HACER", "HALCON", "HELICOPTERO", "HELADO", "HERMANA", "HOLA", "HORIZONTE",
"HURACAN", "IDEAL", "IGLESIA", "ILUMINAR", "IMAGEN", "IMPULSO", "INVIERNO", "JARDIN", "JIRAFA", "JUEGO",
"JUGUETE", "JULIO", "JUPITER", "LADRILLO", "LAGUNA", "LANA", "LAPIZ", "LENTE", "LIMA", "LIVIANO",
"LLAVE", "LLUVIA", "MAIZ", "MALDICION", "MANTEQUILLA", "MARIPOSA", "MASA", "MASTIL", "MATEMATICA", "MEDALLA",
"MELON", "MENSAJE", "MIERDA", "MOLDE", "MONEDA", "MONJE", "MONTAÑA", "MOTOR", "MUSEO", "NADADOR",
"NAVE", "NEVE", "NIEVE", "NINERA", "NUBE", "OCULTO", "OCEANO", "OFICINA", "OLIMPO", "OLIVA",
"ORIGINAL", "ORQUIDEA", "OJO", "PAGINA", "PAIS", "PALOMA", "PAN", "PANTALLA", "PARAISO", "PASEO",
"PATIN", "PEZ", "PIANO", "PILOTO", "PLATO", "PLAZA", "PLOMO", "PODER", "POLVO", "PUERTA",
"PULPO", "QUESO", "RAIZ", "REGLA", "RELOJ", "REMITA", "RIGOR", "RINCÓN", "ROBLE", "ROSA",
"RUGBY", "SAL", "SANDWICH", "SATURNO", "SELVA", "SEQUOIA", "SILLA", "SIRENA", "SOMBRERO", "SUSTITUTO",
"TAQUILLA", "TERA", "TERRENO", "TIGRE", "TOLERANCIA", "TORO", "TOSTADA", "TRABAJO", "TRIANGULO", "URUGUAY",
"VACIO", "VAGABUNDO", "VALLE", "VEHICULO", "VENADO", "VERANO", "VERDURA", "VIA", "VIOLIN", "ZANAHORIA",
"ZAPATO", "ZONDA", "ZORRO", "ZUMO", "ABADIA", "ABISPA", "ACERA", "ADULTO", "AGUA", "ALCALDE",
"ALERCE", "ALFA", "ALGA", "ALMIRANTE", "ALUMNO", "AMETRALLADORA", "ANEXO", "ANILLO", "ANOCHE", "AROMA",
"ASTRONAUTA", "ATENCION", "AURORA", "AVISO", "AYUDA", "BANDERA", "BARBACOA", "BASURA", "BENDICION", "BERENJENA",
"BOCINA", "BOLIGRAFO", "BOSQUE", "BRAZALETE", "BURBUJA", "CALIBRE", "CAMPUS", "CANDELA", "CANDADO", "CARNIVAL",
"CARPA", "CASTIGO", "CELEBRACION", "CENCERRO", "CERCANO", "CHALICE", "CHAMBA", "CHAMPAGNE", "CHOQUE", "CIEGO",
"CLUB", "CONEJERA", "CONQUISTA", "CORNETA", "CUESTA", "CUMPLE", "DESEO", "DIALECTO", "DIGNIDAD", "DILIGENCIA",
"DIPLOMA", "DOLINA", "DOLOR", "DURAZNO", "EDIFICIO", "ENCUENTRO", "EQUIPO", "ERUPCION", "EXPLORADOR", "FELICIDAD",
"FLORES", "FLUIDO", "FOLLETO", "FORNITURA", "FRAGMENTO", "GAVILAN", "GENIAL", "GLAMOUR", "GORRA", "HABITUAL",
"HEROE", "HOGAR", "HONOR", "IMPERIO", "INMIGRANTE", "INOVACION", "INSPIRACION", "ISLA", "JUEGO", "JUPITER",
"KARATE", "KIOSCO", "LAGUNA", "LAMPARA", "LAVADORA", "LEON", "LIRIO", "LOCURA", "LUCHA", "MAQUINA",
"MATRIZ", "MEDIO", "MISTERIO", "MONTANA", "MUNDO", "NAVE", "NUBE", "NUCLEO", "NUMERO", "OCASION",
"ORIGEN", "PAQUETE", "PEQUEÑO", "PERLA", "PESCA", "PLAZA", "POLICIA", "PREDICAR", "RAYO", "RODILLA",
"SABOR", "SADISMO", "SAL", "SALSA", "SALVADOR", "SANDALIAS", "SECRETO", "SENCILLEZ", "TAMBO", "TELEFONO",
"TEMPERATURA", "TENDENCIA", "TERCER", "TONO", "TRAPECIO", "UVA", "VACUNA", "VALLE", "VESTIDO", "VIENTO",
"ZAFIRO", "ZINC", "ZONA", "ZUMBA"

]

# Clase para gestionar el tablero
class Board:
    def __init__(self, size=15):
        self.size = size
        self.board = np.full((size, size), "0")  # Usamos "0" para indicar espacios vacíos
        self.center = (size // 2, size // 2)  # Centro del tablero

    def place_word(self, coord, orientation, word):
        x, y = coord
        word_length = len(word)

        if orientation == "h":
            if y + word_length > self.size:
                return False
            for i in range(word_length):
                if self.board[x, y + i] != "0" and self.board[x, y + i] != word[i]:
                    return False
            for i in range(word_length):
                self.board[x, y + i] = word[i]
        else:  # vertical
            if x + word_length > self.size:
                return False
            for i in range(word_length):
                if self.board[x + i, y] != "0" and self.board[x + i, y] != word[i]:
                    return False
            for i in range(word_length):
                self.board[x + i, y] = word[i]
        return True

    def print_board(self):
        for row in self.board:
            print(" ".join(row).replace("0", "-"))


# Clase para gestionar las letras y la bolsa
class LetterBag:
    def __init__(self):
        self.letters = self.initialize_letters()

    def initialize_letters(self):
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
        count = min(count, len(self.letters))  # Asegúrate de no seleccionar más letras de las que hay
        drawn_letters = random.sample(self.letters, count)
        for letter in drawn_letters:
            self.letters.remove(letter)
        return drawn_letters

    def exchange_letters(self, letters_to_exchange):
        # Verifica que no se intente cambiar más letras de las que tiene el jugador
        for letter in letters_to_exchange:
            if letter not in self.letters:
                return []

        # Retira las letras que se van a intercambiar
        for letter in letters_to_exchange:
            self.letters.remove(letter)

        # Asegúrate de que no se intente sacar más letras de las que hay disponibles
        count_to_draw = min(len(letters_to_exchange), len(self.letters))
        new_letters = self.draw_letters(count_to_draw)

        # Devuelve las letras nuevas al jugador
        return new_letters


# Clase para la IA
class ScrabbleAI:
    def __init__(self):
        self.used_words = set()

    def best_move(self, board, tiles):
        for word in dictionary:
            if word not in self.used_words and set(word).issubset(tiles):
                for x in range(board.size):
                    for y in range(board.size):
                        for orientation in ['h', 'v']:
                            if board.place_word((x, y), orientation, word):
                                self.used_words.add(word)
                                return (word, (x, y), orientation)
        return None

    def exchange_turn(self, letter_bag, tiles):
        # La IA decide si quiere cambiar letras
        if len(tiles) > 0:  # Solo cambia letras si tiene alguna
            letters_to_exchange = random.sample(tiles, min(len(tiles), 7))  # Cambia todas las letras o menos
            print(f"La IA cambia las letras: {', '.join(letters_to_exchange)}")
            new_letters = letter_bag.exchange_letters(letters_to_exchange)
            return new_letters
        return tiles  # Si no tiene letras, no cambia nada


# Clase principal para gestionar el juego
class ScrabbleGame:
    def __init__(self):
        self.board = Board()
        self.bag = LetterBag()
        self.players = ["Jugador", "IA"]
        self.player_tiles = {player: self.bag.draw_letters(7) for player in self.players}
        self.current_player_index = 0
        self.ai = ScrabbleAI()

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"\nTurno de {current_player}")

        if current_player == "IA":
            best_move = self.ai.best_move(self.board, self.player_tiles["IA"])
            if best_move:
                word, coord, orientation = best_move
                self.board.place_word(coord, orientation, word)
                print(f"La IA coloca la palabra '{word}' en {coord} ({orientation})")
                self.player_tiles["IA"] = self.bag.draw_letters(7)
            else:
                # La IA no tiene un movimiento válido, intenta cambiar letras
                new_letters = self.ai.exchange_turn(self.bag, self.player_tiles["IA"])
                self.player_tiles["IA"] = new_letters
                print("La IA no puede jugar, ha cambiado sus letras.")
        else:
            self.human_turn()

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def human_turn(self):
        print(f"Tus letras: {', '.join(self.player_tiles['Jugador'])}")

        while True:
            action = input("¿Quieres jugar una palabra, cambiar letras o pasar tu turno? (j/c/p): ").lower()
            if action == 'c':
                letters_to_exchange = input("Ingrese las letras que desea cambiar (sin espacios): ").upper()
                letters_to_exchange = list(letters_to_exchange)

                if all(letter in self.player_tiles["Jugador"] for letter in letters_to_exchange):
                    # Realiza el intercambio de letras
                    new_letters = self.bag.exchange_letters(letters_to_exchange)

                    # Actualiza el atril del jugador con las nuevas letras
                    for letter in letters_to_exchange:
                        self.player_tiles["Jugador"].remove(letter)

                    # Agrega las nuevas letras al atril del jugador
                    self.player_tiles["Jugador"].extend(new_letters)

                    print(f"Has cambiado las letras: {', '.join(letters_to_exchange)}")
                    return  # Finaliza el turno

                else:
                    print("No tienes algunas de las letras que intentas cambiar.")
                    continue

            elif action == 'j':
                word = input("Ingrese la palabra: ").upper()
                if word not in dictionary or not set(word).issubset(self.player_tiles["Jugador"]):
                    print("Palabra no válida o no tienes las letras necesarias.")
                    continue
                
                coord = input("Ingrese la coordenada (fila,columna): ")
                x, y = map(int, coord.split(','))
                orientation = input("Ingrese la orientación (h/v): ").lower()
                if orientation not in ['h', 'v']:
                    print("Orientación no válida.")
                    continue

                if self.board.place_word((x, y), orientation, word):
                    print(f"Colocas la palabra '{word}' en ({x}, {y}) {orientation}.")
                    for letter in word:
                        self.player_tiles["Jugador"].remove(letter)
                    self.player_tiles["Jugador"].extend(self.bag.draw_letters(7 - len(self.player_tiles["Jugador"])))
                    break
                else:
                    print("No se puede colocar la palabra. Intente de nuevo.")
            elif action == 'p':
                print("Has pasado tu turno.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def check_game_over(self):
        return len(self.bag.letters) == 0 and all(len(tiles) == 0 for tiles in self.player_tiles.values())


# Ejecución del juego
if __name__ == "__main__":
    game = ScrabbleGame()

    while not game.check_game_over():
        game.board.print_board()
        game.play_turn()

    print("El juego ha terminado.")
