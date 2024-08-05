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

def main():
    Juego = Game(azul=(Fore.BLUE + " O "), rojo=(Fore.RED + " O "), amarillo=(Fore.YELLOW + " O "), verde=(Fore.GREEN + " O "), reset=Fore.RESET)
    Juego.elegirModo()
if __name__ == "__main__":
    # Inicializador del archivo.
    main()