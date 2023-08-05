def separa_letras(cadena):
    # Comprobar que parámetro es un string
    if not isinstance(cadena, str):
        return -100, None, None
        # Código de error -100, luego sale dos veces None

    # Comprobar que el string no está vacío
    if not cadena:
        return -300, None, None
        # Código de error -300, luego sale dos veces None

    # Comprobar que el string contiene solo letras
    if not cadena.isalpha():
        return -200, None, None
        # Código de error -200, luego sale dos veces None

    # Separar el string en mayúsculas y minúsculas
    may = ''.join(c for c in cadena if c.isupper())
    min = ''.join(c for c in cadena if c.islower())

    return 0, may, min
    # Código de éxito 0, mayúsculas y minúsculas


def potencia_manual(base, potencia):
    # Verificar que los parámetros no sean de tipo string
    if isinstance(base, str) or isinstance(potencia, str):
        return -400, None
        # Código de error -400, resultado None

    # Función para calcular la potencia manual
    def calcular_potencia(base, potencia):
        if potencia == 0:
            # Si la potencia es 0, se retorna 1
            return 1
        if potencia > 0:
            # Si la potencia es mayor a 0, se realiza un ciclo
            resultado = 0
            aux = base
            for i in range(1, potencia):

                for j in range(base):
                    resultado += aux
                aux = resultado
                resultado = 0
            return aux

    # Calcular la potencia utilizando la función recursiva
    resultado1 = calcular_potencia(base, potencia)

    return 0, resultado1
    # Código de éxito 0, resultado de la potencia
