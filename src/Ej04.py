

## Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# El usuario escribe por pantalla un número entero positivo.
# Queremos que esa variable muestre por pantalla la cuenta atrás desde ese número hasta 0 separados por comas.

def escribir_numero():## Entrada 
    
    '''
    Escribimos una variable para que la guardemos, escribiendo un número entero positivo.
    '''
    
    numero = int(input("Escribe un número entero positivo:\n--->"))
    return numero

def cuenta_atras(numero):## Procesamiento

    '''
    Aquí llamamos a numero para poder hacer el siguiente procedimiento.
    '''
    cuenta = ""

    for x in range(numero, -1, -1 ):

        cuenta += str(x) + ", "
    cuenta = cuenta[:-2] # Me salia siempre con una comilla y un espacio al final del resultado y esta es la solución, lo que hacemos es quitar esos dos huecos poniendo el '-2', si quisiéramos quitar más, más alto sería el caracter.
    
    return cuenta

def salida(cuenta):## Salida

    '''
    Llamamos a cuenta para poder mostrar por pantalla el resultado del procesamiento.
    '''    
    print(cuenta)


def main():

    #Entrada
    numero = escribir_numero()

    #Procesamiento
    cuenta = cuenta_atras(numero)
    
    #Salida
    salida(cuenta)

if __name__ == "__main__":

    main()