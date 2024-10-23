## Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# El usuario escribe por pantalla una palabra y nosotros la guardamos en una variable.
# Queremos que esa variable se repuita 10 veces

def escribir_palabra():## Entrada 
    
    '''
    Escribimos una variable para que el usuario escriba la palabra que desee.
    '''
    
    palabra = input("Escribe una palabra por pantalla:\n--->")
    return palabra

def repetir_diez(palabra):## Procesamiento

    '''
    Aquí llamaremos a la variable palabra para poder hacer que esta se repita 10 veces.
    '''

    respuesta = ""

    for x in range(10):

        respuesta += str(x) + "." + palabra +"\n"

    return respuesta

def salida(respuesta):## Salida

    '''
    Llamaremos a respuesta, para que muestre la repetición de esa palabra.
    '''    
    print(respuesta)


def main():

    #Entrada
    palabra = escribir_palabra()

    #Procesamiento
    respuesta = repetir_diez(palabra)
    
    #Salida
    salida(respuesta)

if __name__ == "__main__":

    main()