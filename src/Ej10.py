## Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

# El usuario escribe por pantalla una palabra y nosotros la guardamos en una variable.
# Queremos que esa variable muestre por pantalla si es primo o no.

def escribir_numero():  # Entrada

    '''
    Pedimos al usuario que escriba un número entero.
    '''

    numero = int(input("Escribe un número entero:\n---> "))

    return numero

def es_primo(numero):  # Procesamiento

    '''
    Comprueba si el número ingresado es primo.
    '''

    if numero <= 1:

        return False  
    
    for x in range(2, int(numero * 0.5) + 1):

        if numero % x == 0:

            return False  # El número es divisible, por lo tanto no es primo
        
    return True  # Si no se encontró ningún divisor, es primo

def salida(numero, primo):  # Salida

    '''
    Mostramos si el número es primo o no.
    '''

    if primo:

        print(numero, "es un número primo.")

    else:

        print(numero, "no es un número primo.")

def main():

    # Entrada
    numero = escribir_numero()
    
    # Procesamiento
    primo = es_primo(numero)
    
    # Salida
    salida(numero, primo)

if __name__ == "__main__":
    main()
