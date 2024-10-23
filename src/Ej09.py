## Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

## Escribir un programa que almacene la cadena de caracteres contraseña en una variable.
## pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def escribir_contraseña():  # Entrada

    '''
    Le pedimos al usuario que Escriba la contraseña.
    '''

    contraseña = input("Escribe la contraseña:\n---> ")

    return contraseña

def comprobar_contraseña():  # Procesamiento

    '''
    Escribe la contraseña y comprueba si es correcta.
    '''

    contraseñavalida = "aaron"  
    contraseña = "" 

    while contraseña != contraseñavalida:

        contraseña = escribir_contraseña() 

        if contraseña != contraseñavalida:

            salida("Contraseña incorrecta.")

    return "¡Contraseña correcta!" 

def salida(mensaje):  # Salida

    '''
    Muestra el mensaje por pantalla.
    '''

    print(mensaje)

def main():

    '''
    Función principal que coordina la entrada, procesamiento y salida.
    '''

    mensaje = comprobar_contraseña()  # Procesamiento
    
    salida(mensaje)  # Salida

if __name__ == "__main__":
    main()
