## Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

# El usuario escribe por pantalla un número entero positivo.
# Queremos que esa variable muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def escribir_numero():## Entrada 
    
    '''
    Escribimos una variable para que la guardemos, escribiendo un número entero positivo.
    '''
    
    numero = int(input("Escribe un número entero positivo:\n--->"))
    return numero

def numeros_impares(numero):## Procesamiento

    '''
    Aquí llamamos a numero para poder hacer el siguiente procedimiento.
    '''
    impares = ""

    for x in range(1, numero + 1, 2 ):

        impares += str(x) + ", "
    impares = impares[:-2] # Me salia siempre con una comilla y un espacio al final del resultado y esta es la solución, lo que hacemos es quitar esos dos huecos poniendo el '-2', si quisiéramos quitar más, más alto sería el caracter.
    
    return impares

def salida(impares):## Salida

    '''
    Llamamos a impares para poder mostrar por pantalla el resultado del procesamiento.
    '''    
    print(impares)


def main():

    #Entrada
    numero = escribir_numero()

    #Procesamiento
    impares = numeros_impares(numero)
    
    #Salida
    salida(impares)

if __name__ == "__main__":

    main()