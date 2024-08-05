from colorama import Fore
from time import sleep
import keyboard
import random
class Game:
    #Juego, dividido en sus respectivas clases y métodos.
    def __init__(self, rojo, azul, verde, amarillo, reset):
        self.rojo = rojo
        self.azul = azul
        self.verde = verde
        self.amarillo = amarillo
        self.reset = reset
       
        self.secuencia = []
        self.intentoDeAdivinarSecuencia = []
        
    def elegirModo(self):
        while True:
            respuesta = input(f'¿Adivinas o creas la secuencia? (Adivinar / Crear): ').strip().lower()
            if respuesta not in ('adivinar', 'crear'):
                print("Agrega una respuesta correcta.")
            else:
                if respuesta == 'adivinar':
                    self.creaComputadora()
                elif respuesta == 'crear':
                    self.creaJugador()
                break
    def creaJugador(self):
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        while True:
            opcion = input("Elige los colores de tu secuencia (r/b/y/g)")
            if len(self.secuencia) <= 4:
                match opcion:
                    case "r":
                        self.secuencia.append(posiblesOpciones[0])
                        print("|", "".join(self.secuencia) + self.reset, "|")
                    case "b":
                        self.secuencia.append(posiblesOpciones[1])
                        print("|", "".join(self.secuencia) + self.reset, "|")
                    case "y":
                        self.secuencia.append(posiblesOpciones[2])
                        print("|", "".join(self.secuencia) + self.reset, "|")
                    case "g":
                        self.secuencia.append(posiblesOpciones[3])
                        print("|", "".join(self.secuencia) + self.reset, "|")
                    case _:
                        print("Introduzca una respuesta correcta.")
                        #En caso de haber alcanzado el limite de espacio.
                if len(self.secuencia) == 4:
                    confirm = input(f"¿Confirmar secuencia? (S/N): ").strip().lower()
                    if confirm == "s":
                        self.eleccionAzar()
                        break
                    else:
                        self.secuencia = []
        return self.secuencia
    def creaComputadora(self):
        while True:
            posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
            self.secuencia.insert(1, random.choice(posiblesOpciones) + self.reset)
            if len(self.secuencia) == 4:
                print(''.join(self.secuencia) + self.reset)
                self.eleccionJugador()
                break
    def eleccionAzar(self):
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        eleccionComputadora = []
        intentos = 0
        while True:
            if intentos == 12:
                print(f"La computadora no ha podido adivinar. ¡Has ganado!")
                break
            else:
                sleep(1)
                intentos += 1
                print(f"Intento: {intentos}")
                eleccionComputadora = [random.choice(posiblesOpciones) for _ in range(4)]
                print('La elección de la computadora es: ', ''.join(eleccionComputadora) + self.reset)
                if eleccionComputadora == self.secuencia:
                    print("¡La computadora ha ganado!")
                    print(''.join(eleccionComputadora))
                    break
    def eleccionJugador(self):
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        eleccionJugador = []
        intentos = 0
        while True:
            if intentos == 12:
                print("Número máximo de intentos alcanzado.")
                break
            else:
                opcion = input("Elige los colores de tu secuencia (r/b/y/g). Para terminar la secuencia, escribe 'done': ").strip().lower()
                if opcion == 'done' and len(eleccionJugador) == 4:
                    print("Secuencia finalizada.")
                    print("|", "".join(eleccionJugador) + self.reset, "|")
                    break
                if len(eleccionJugador) >= 4:
                    print("Ya has elegido 4 colores. Para finalizar, escribe 'done'.")
                match opcion:
                    case "r":
                        eleccionJugador.append(posiblesOpciones[0])
                    case "b":
                        eleccionJugador.append(posiblesOpciones[1])
                    case "y":
                        eleccionJugador.append(posiblesOpciones[2])
                    case "g":
                        eleccionJugador.append(posiblesOpciones[3])
                    case _:
                        print("Introduzca una respuesta correcta.")
                print("|", "".join(eleccionJugador) + self.reset, "|")
                intentos += 1
                if len(eleccionJugador) == 4:
                    print("Final...")
                    print("|", "".join(eleccionJugador) + self.reset, "|")
                    break
def main():
    Juego = Game(azul=(Fore.BLUE + " O "), rojo=(Fore.RED + " O "), amarillo=(Fore.YELLOW + " O "), verde=(Fore.GREEN + " O "), reset=Fore.RESET)
    Juego.elegirModo()
if __name__ == "__main__":
    # Inicializador del archivo.
    main()

