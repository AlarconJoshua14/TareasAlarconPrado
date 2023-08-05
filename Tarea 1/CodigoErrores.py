def calcular_promedio(nums):
    suma = 0
    cantidad = len(nums)

    for num in nums:
        suma += num
        promedio = suma / cantidadd  # Error 1: Variable mal escrita (cantidadd en lugar de cantidad)

    promedio = suma / cantidad
    return promedio  # Error 2: Falta de espacio antes del comentario


numeros = [5, 10, 15, 20, 25]
resultado = calcular_promedio(numeros)
print("El promedio es:", resultado)  # Error 3: Falta espacio después de la coma
