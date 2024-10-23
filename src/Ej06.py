

'''
 Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
'''
# Pedimos al usuario un número entero.
# Con ese número entero, foramos un triángulo rectángulo.

def escribir_numero():  # Entrada 

    '''
    Escribimos una variable para que la guardemos, escribiendo un número entero positivo.
    '''

    numero = int(input("Escribe por pantalla un número entero positivo:\n---> "))
    return numero

def mostrar_triangulo(numero):  # Procesamiento

    '''
    Mostramos por pantalla un triángulo rectángulo con la altura que hayamos puesto en la entrada.
    '''

    triangulo = ""

    for x in range(1, numero + 1):

        triangulo += "*" * x + "\n" 

    return triangulo

def salida(triangulo):  # Salida

    '''
    Llamamos a la variable triangulo para poder mostrar por pantalla el resultado del procesamiento.
    '''    

    print(triangulo)

def main():

    # Entrada

    numero = escribir_numero()
    
    # Procesamiento

    triangulo = mostrar_triangulo(numero)
    
    # Salida

    salida(triangulo)

if __name__ == "__main__":
    
    main()
