def imprimir_tablero() 
   Muestra el tablero de juego en la consola,
   mostrando los colores que se elijen cuando se juega

actualizar_tablero()
    Actualiza el tablero con el resultado de cada intento

def elegirModo()
    Permite al jugador elegir entre dos modos de juego: "Adivinar" o "Crear".
    Dependiendo de la elección, se realiza el juego segun el modo elejigo

 def convertir_colores()
    Convierte una secuencia de caracteres de colores ('r', 'b', 'y', 'g') 
    en sus representaciones de color correspondientes utilizando colorama.

def valida_secuencia()
    Valida que la eleccion sea de 4 colores
    y que todos sean válidos

def creaJugador()
    hace al jugador crear una secuencia de colores.Se valida y se confirma antes de seguir,
    Si se confirma, el juego continúa con la computadora intentando adivinar el codigo.

 def creaComputadora()
   La computadora crea una secuencia aleatoria, para que el jugador la adivine

 def eleccionAzar()
    La computadora intenta adivinar el codigo creado. se muestra los intentos de la compu,
    si gana termina el juego, se queda sin intentos
  
eleccionJugador()
    Hace que el jugador intente adivinar la secuencia de la computadora
    Se validan los intentos y se muestrn en consola 
    El juego termina si se adivina el codigo, o se acaban los intentos

if __name__ == "__main__":
Ejecuta la funcion main() .Solo si el archivo se ejecuta directamente, no si se importa desde otro módulo.
    main()


funcion def main():
    Inicializa el juego con colores formateados y llama al método juego.elegirModo()
    para que el usuario elija el modo de juego.


