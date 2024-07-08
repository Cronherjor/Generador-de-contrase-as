import random
import string

# Bloque try-except para manejar la entrada del usuario y posibles errores
try:
    # Solicitar al usuario que ingrese la longitud de la contraseña y convertirla a un entero
    longitud = int(input("Ingrese la longitud de la contraseña: "))

    # Verificar si la longitud es un número entero positivo
    if longitud <= 0:
        # Si la longitud es menor o igual a 0, lanzar una excepción ValueError con un mensaje personalizado
        raise ValueError("Longitud debe ser un número entero positivo.")
except ValueError as e:
    # Capturar y manejar la excepción ValueError, imprimiendo el mensaje de error
    print(e)

# Definición de la función GeneradorContrasena que genera una contraseña aleatoria
def GeneradorContrasena(longitud):
    # Definir las cadenas de caracteres que se pueden utilizar para generar la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Generar una contraseña aleatoria utilizando la longitud y la cadena de caracteres definidas anteriormente
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

# Generar y mostrar la contraseña solo si la variable 'longitud' está definida y es válida en el ambito local
if 'longitud' in locals():
    print(f"La contraseña generada es: {GeneradorContrasena(longitud)}")


    '''  ''.join(...): Toma todos los caracteres seleccionados aleatoriamente y los une en una sola cadena 
    sin ningún separador (por eso se usa '', una cadena vacía, para la unión). Esencialmente, convierte una lista de caracteres en una cadena.'''

    ''' for i in range(longitud): Repite la selección de caracteres aleatorios longitud veces '''