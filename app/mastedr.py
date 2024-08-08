from colorama import Fore
from time import sleep
import random

class Game:

    #     self rojo: Representa el color rojo en formato colorama
    #     self azul: Representa el color azul en formato colorama
    #     self verde: Representa el color verde en formato colorama
    #     self amarillo: Representa el color amarillo en formato colorama
    #     self reset: Secuencia de reset de color para volver al color normal
    def __init__(self, rojo, azul, verde, amarillo, reset):
        self.rojo = rojo
        self.azul = azul
        self.verde = verde
        self.amarillo = amarillo    
        self.reset = reset
        self.secuencia = []
        self.intentoDeAdivinarSecuencia = []
        self.tablero = [["O" for _ in range(4)] for _ in range(12)] 

   
    def imprimir_tablero(self):
        print("Tablero de juego:")  # funcion que muestra la tabla en consola
        for fila in self.tablero:
            print(' | '.join(fila))
        print()



        #Actualiza el tablero con el resultado de cada intento
        #fila: La fila en la que se debe actualizar el tablero
        
    def actualizar_tablero(self, intento, fila):
        if 0 <= fila < len(self.tablero):
            resultado = []
            secuencia_restante = self.secuencia[:]  

            for i in range(4):
                if intento[i] == self.secuencia[i]:
                    resultado.append(Fore.GREEN + intento[i] + self.reset)
                    secuencia_restante[i] = None  

            for i in range(4):
                if intento[i] != self.secuencia[i]:
                    if intento[i] in secuencia_restante:
                        resultado.append(Fore.RED + intento[i] + self.reset)
                        secuencia_restante[secuencia_restante.index(intento[i])] = None
                    else:
                        resultado.append(Fore.BLACK + intento[i] + self.reset)
     
            self.tablero[fila] = resultado
            self.imprimir_tablero()
        else:
            print("Número de fila inválido.")
    
    def elegirModo(self):
        while True:
            respuesta = input('¿Adivinas o creas la secuencia? (Adivinar / Crear): ').strip().lower()
            if respuesta == 'adivinar':
                self.creaComputadora() #Permite al jugador elegir el modo de juego: 'Adivinar' o 'Crear'.
                break
            elif respuesta == 'crear':
                self.creaJugador()
                break
            else:
                print("Respuesta no válida. Elige 'Adivinar' o 'Crear'.")

    def convertir_colores(self, secuencia):
          # Convierte una secuencia de caracteres de colores a su representación en formato colorama
        #returna una lista de color en formato colorama
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        colores = {
            "r": posiblesOpciones[0],
            "b": posiblesOpciones[1],
            "y": posiblesOpciones[2],
            "g": posiblesOpciones[3]
        }
        return [colores.get(color, None) for color in secuencia]

    def valida_secuencia(self, secuencia):
         #Valida que la secuencia de colores tenga exactamente 4 colores y que todos sean correctos
         #Se valida la secuencia de colores
         # return True si la secuencia es válida, False en caso contrario
         # se confirma si esta seguro de la secuencia a colocar
        return len(secuencia) == 4 and all(color in {"r", "b", "y", "g"} for color in secuencia)

    def creaJugador(self):
        #Permite al jugador crear una secuencia de colores La secuencia es validada y confirmada antes de continuar
        while True:
            opcion = input("Elige los colores de tu secuencia (r/b/y/g)separados por comas: ").strip().lower()
            secuencia = opcion.split(',')
            if self.valida_secuencia(secuencia):
                self.secuencia = self.convertir_colores(secuencia)
                print("|", "".join(self.secuencia) + self.reset, "|")
                confirm = input(f"¿Confirmar secuencia? (S/N): ").strip().lower()
                if confirm == "s":
                    self.eleccionAzar()
                else:
                    self.secuencia = []
            else:
                print("Introduzca exactamente 4 colores válidos (r/b/y/g).")
                
    def creaComputadora(self):  
        #Genera una secuencia aleatoria de colores para la computadora y permite al jugador intentar adivinarla     
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        self.secuencia = [random.choice(posiblesOpciones) for _ in range(4)]
        print('Combinación de la computadora es: ', ''.join(self.secuencia) + self.reset)
        self.eleccionJugador()
    
    def eleccionAzar(self):
        #La computadora hace intentos aleatorios para adivinar la secuencia del jugador. El tablero se actualiza con cada intento.
        # muestra si gana la computadora o ha perdido
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        for intento in range(12):
            sleep(1)
            print(f"Intento de la computadora: {intento + 1}")
            eleccionComputadora = [random.choice(posiblesOpciones) for _ in range(4)]
            print('La elección de la computadora es: ', ''.join(eleccionComputadora) + self.reset)
            self.actualizar_tablero(eleccionComputadora, intento) 
            
            if eleccionComputadora == self.secuencia:
                print("¡La computadora ha ganado!")
                print(''.join(eleccionComputadora))
                break
        else:
            print("La computadora no ha podido adivinar. ¡Has ganado!")

    def eleccionJugador(self):
       # Permite al jugador hacer intentos para adivinar la secuencia generada por la computadora. El tablero se actualiza con cada intento
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        for intento in range(12):
            opcion = input("Elige los colores de tu secuencia (r/b/y/g) separados por comas (ej. r,b,g,y) o escribe 'done' para terminar: ").strip().lower()
            if opcion == 'done' and len(self.intentoDeAdivinarSecuencia) == 4:
                print("Secuencia finalizada.")
                print("|", "".join(self.intentoDeAdivinarSecuencia) + self.reset, "|")
                break

            secuencia = opcion.split(',')
            if self.valida_secuencia(secuencia):
                self.intentoDeAdivinarSecuencia = self.convertir_colores(secuencia)
                self.actualizar_tablero(self.intentoDeAdivinarSecuencia, intento)
                if self.intentoDeAdivinarSecuencia == self.secuencia:
                    print("¡Has ganado!")
                    break
                else:
                    print("Inténtalo de nuevo.")                    
            else:
                print("Debe ingresar exactamente 4 colores válidos (r/b/y/g).")
        else:
            print("Número máximo de intentos alcanzado.")

def main():
    #Función que inicializa el juego y permite al jugador elegir el modo
    juego = Game(
        azul=(Fore.BLUE + " O "),
        rojo=(Fore.RED + " O "),
        amarillo=(Fore.YELLOW + " O "),
        verde=(Fore.GREEN + " O "),
        reset=Fore.RESET
    )
    juego.elegirModo()

if __name__ == "__main__":
    main()
