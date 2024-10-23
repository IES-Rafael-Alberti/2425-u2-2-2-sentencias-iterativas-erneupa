

## Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# El usuario escribe por pantalla la cantidad a invertir, el interés anual y número de años.
# Queremos que esa variable muestre por pantalla el capital obtenido cada año invertido.

def escribir_cantidad():  ## Entrada 
    '''
    Pedimos al usuario la cantidad a invertir y la devuelve.
    '''
    cantidad = float(input("Escribe la cantidad a invertir:\n---> "))
    return cantidad

def escribir_interes():  ## Entrada 
    '''
    Pedimos al usuario el interés anual y lo devuelve.
    '''
    interes = float(input("Escribe el interés anual (en %):\n---> "))
    return interes

def escribir_anios():  ## Entrada 
    '''
    Pedimos al usuario el número de años y lo devuelve.
    '''
    años = int(input("Escribe el número de años de la inversión:\n---> "))
    return años

def calcular_capital(cantidad, interes, anios):  ## Procesamiento
    '''
    Calculamos llamando a las tres variables, el capital obtenido cada año.
    '''
    capital_por_año = ""
    for x in range(1, anios + 1):
        cantidad *= (1 + (interes/100))  # Actualiza la cantidad con el interés
        capital_por_año += "Año " + str(x) + ": " + str(cantidad) + " €" + "\n"
    return capital_por_año

def salida(capital):  ## Salida
    '''
    Mostramos por pantalla el capital obtenido cada año.
    '''    
    print("Capital obtenido en cada año de inversión: \n",capital)
    

def main():
    # Entrada
    cantidad = escribir_cantidad()
    interes = escribir_interes()
    años = escribir_anios()

    # Procesamiento
    capital = calcular_capital(cantidad, interes, años)
    
    # Salida
    salida(capital)

if __name__ == "__main__":
    main()
