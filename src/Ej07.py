## Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# Mostraremos la tabla del 1.
# Hacemos un procedimiento para que x vaya sumando de uno en uno y luego se multiplique por 1.

def mostrar_tabla():  # Procesamiento

    '''
    Mostramos por pantalla La tabla de multiplicar del 1.
    '''

    tabla = ""

    for x in range(1, 10 + 1):

        tabla += ("1 por " + str(x) + " = ") + 1 * str(x) + "\n" 

    return tabla

def salida(tabla):  # Salida

    '''
    Llamamos a la variable tabla para poder mostrar por pantalla el resultado del procesamiento.
    '''    

    print("A continuación la tabla del 1:\n", tabla)

def main():
  
    # Procesamiento

    tabla = mostrar_tabla()
    
    # Salida

    salida(tabla)

if __name__ == "__main__":
    
    main()
