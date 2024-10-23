## Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# El usuario escribe por pantalla su edad y nosotros la guardamos en una variable.
# Queremos que esa variable muestre por pantalla todos los años cumplidos.

def escribir_edad():## Entrada 
    
    '''
    Escribimos una variable para que el usuario escriba su edad.
    '''
    
    edad = int(input("Escribe tu edad por pantalla:\n--->"))
    return edad

def años_cumplidos(edad):## Procesamiento

    '''
    Para que muestre todos los años cumplidos, atribuimos la bariable edad para poder hacer un rango del 1 hasta su edad.
    '''
    años=""

    for x in range(1, edad + 1):
        años += str(x) + "\n"
    return años

def salida(años):## Salida

    '''
    Mostramos por pantalla todos los años cumplidos devolviendo años.
    '''    
    print(años)


def main():

    #Entrada
    edad = escribir_edad()

    #Procesamiento
    años = años_cumplidos(edad)
    
    #Salida
    salida(años)

if __name__ == "__main__":

    main()