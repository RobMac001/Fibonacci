import time # Libreria para calcular el tiempo de ejecucion


def tiempo_exponencial(a, b): # Esta función realiza la multiplicación de dos matrices
    result = [[0, 0], [0, 0]]
    for i in range(2): # Utiliza tres bucles anidados para recorrer los elementos de las matrices
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result # Retorna el resultado de la matriz


def conversion_matrices(matrix, n): # Eleva la matriz a la potencia n
    result = [[1, 0], [0, 1]]
    while n > 0: # Itera mientras n sea mayor que 0
        if n % 2 == 1: # Verifica si es impar
            result = tiempo_exponencial(result, matrix) # si es asi multiplica result por la matriz original
        matrix = tiempo_exponencial(matrix, matrix)
        n //= 2
    return result # Retorna el resultado de la matriz


def divideyvenceras(base, exponent): # Toma el parametro de la Base y el exponente
    if exponent == 0: #Verifica si el exponente es igual a 0
        return 1
    elif exponent % 2 == 0: # Si el exponente es par, divide y conquista
        # calcula recursivamente la mitad del exponente y multiplica el resultado por sí mismo
        half_divideyvenceras = divideyvenceras(base, exponent // 2)
        return half_divideyvenceras * half_divideyvenceras
    else: # Si el exponente es impar, divide y vence y luego multiplica por la base
        half_divideyvenceras = divideyvenceras(base, (exponent - 1) // 2)
        return base * half_divideyvenceras * half_divideyvenceras


def fibonacci_exponencial(n): # Calcula el n-ésimo término de la secuencia de Fibonacci
    start_time = time.perf_counter()

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        base = [[1, 1], [1, 0]] # Inicializa la matriz base
        result_matrix = conversion_matrices(base, n - 1) # conversion_tiempo_lineal eleva la matriz base a la n-1
        result = result_matrix[0][0]

    end_time = time.perf_counter() # Reloj de ejecucion del programa
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time:.6f} segundos")

    return result # Retorna el resultado de la matriz


n = int(input("Introduce un valor: ")) # Introduce el valor del usuario
resultado = fibonacci_exponencial(n) # Llama a la funcion principal
print("La secuencia de Fibonacci en tiempo exponencial {} es: {}".format(n, resultado)) # Imprime el resultado

