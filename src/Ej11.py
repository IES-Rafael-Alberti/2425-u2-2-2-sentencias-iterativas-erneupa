## Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

# Le pedimos al usuario que escriba una palabra.
# Le mostramos todas olas letras en cadena empezando por la última, una a una.

def escribir_palabra(): ## Entrada 
    
    '''
    Introducimos una variable para que el usuario escriba una palabra.
    '''
    
    palabra = input("Escribe palabra:\n--->")
    return palabra

def letras_mostradas(palabra): ## Procesamiento

    '''
    Para que muestre todas las letras llamamos a lavariable.
    '''

    letras=""

    for x in range(len(palabra) -1, -1, -1):

        letras += palabra[x] + "\n"

    return letras

def salida(letras): ## Salida

    '''
    Mostramos por pantalla todas las letras de la palabra.
    ''' 

    print(letras)


def main():

    #Entrada

    palabra = escribir_palabra()

    #Procesamiento

    letras = letras_mostradas(palabra)
    
    #Salida
    
    salida(letras)

if __name__ == "__main__":

    main()