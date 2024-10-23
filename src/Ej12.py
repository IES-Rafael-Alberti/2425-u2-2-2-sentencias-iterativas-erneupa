## Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

# Pedimos que escriba una palabra.

# Pedimos que escriba una letra.

# Según la palabra y la letra, le mostramos cuantas veces se repite esa letra en la palabra escrita.

def escribir_frase():  # Entrada

    '''
    Pedimos al usuario que introduzca una frase.
    '''

    frase = input("Escribe una frase:\n---> ")

    return frase

def escribir_letra():  # Entrada

    '''
    Pedimos al usuario que introduzca una letra.
    '''

    letra = input("Escribe una letra:\n---> ")

    return letra


def contar_letra(frase, letra):  # Procesamiento

    '''
    Cuenta cuántas veces aparece la letra en la frase.
    '''

    return frase.count(letra) 

def salida(contar):  # Salida

    '''
    Muestra el número de ocurrencias de la letra en la frase.
    '''

    print("La letra aparece", contar, "veces.")

def main():

    # Entrada

    frase = escribir_frase()

    letra = escribir_letra()

    # Procesamiento

    contar = contar_letra(frase, letra)

    # Salida

    salida(contar)

if __name__ == "__main__":

    main()