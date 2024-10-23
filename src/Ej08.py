'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''

# El usuario escribe por pantalla un número entero.
# Queremos que esa variable muestre por pantalla todos los números en un rectgangulo ascendente pero solo los impares.

def escribir_numero(): ## Entrada
   
    """
    Escribimos una variable para que la guardemos, escribiendo un número entero.
    """

    numero = int(input("Escribe un número entero:\n--->"))
    
    return numero

def triangulo(numero): ## Procesamiento
   
    """
    Mostramos por pantalla un triángulo rectangulo llamando a la variable numero.
    """

    resultado = ""

    for x in range(1, numero + 1, 2): 
        
        resultado +=" ".join(str(x) for x in range(x, 0, -2)) + "\n"
       
    return resultado

def salida(resultado): ## Salida

    """
    Llamamos a resultado para mostrar por pantalla el triángulo.
    """

    print(resultado)

def main():

    # Entrada

    numero = escribir_numero()

    # Procesamiento

    resultado = triangulo(numero)

    # Salida

    salida(resultado)

if __name__ == "__main__":
    
    main()