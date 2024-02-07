import time # Libreria para calcular el tiempo de ejecucion


def tiempo_lineal(a, b): # Esta función realiza la multiplicación de dos matrices
    result = [[0, 0], [0, 0]]
    for i in range(2): # Utiliza tres bucles anidados para recorrer los elementos de las matrices
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result # Retorna el resultado de la matriz


def conversion_tiempo_lineal(matriz, n): # Eleva la matriz a la potencia n
    result = [[1, 0], [0, 1]]
    while n > 0: # Itera mientras n sea mayor que 0
        if n % 2 == 1: # Verifica si es impar
            result = tiempo_lineal(result, matriz) # si es asi multiplica result por la matriz original
        matriz = tiempo_lineal(matriz, matriz)
        n //= 2
    return result # Retorna el resultado de la matriz


def fibonacci(n): # Calcula el n-ésimo término de la secuencia de Fibonacci
    if n == 0:
        return 0
    elif n == 1:
        return 1

    base = [[1, 1], [1, 0]] # Inicializa la matriz base
    start_time = time.perf_counter()
    result_matriz = conversion_tiempo_lineal(base, n - 1) # conversion_tiempo_lineal eleva la matriz base a la n-1
    end_time = time.perf_counter()

    execution_time = end_time - start_time # Reloj de ejecucion del programa
    print(f"Tiempo de ejecución: {execution_time:.6f} segundos")

    return result_matriz[0][0] # Retorna el resultado de la matriz


n = int(input("Introduce un valor: ")) # Introduce el valor del usuario
resultado = fibonacci(n) # Llama a la funcion principal
print("La secuencia de Fibonacci de {} es: {}".format(n, resultado)) # Imprime el resultado
