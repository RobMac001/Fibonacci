import time # Libreria para calcular el tiempo de ejecucion


def divideyvenceras(base, exponent): # Toma el parametro de la Base y el exponente
    start_time = time.perf_counter()

    if exponent == 0: #Verifica si el exponente es igual a 0
        result = 1
    elif exponent % 2 == 0: # Si el exponente es par, divide y conquista
        # calcula recursivamente la mitad del exponente y multiplica el resultado por sí mismo
        half_divideyvenceras = divideyvenceras(base, exponent // 2)
        result = half_divideyvenceras * half_divideyvenceras
    else: # Si el exponente es impar, divide y vence y luego multiplica por la base
        half_divideyvenceras = divideyvenceras(base, (exponent - 1) // 2)
        result = base * half_divideyvenceras * half_divideyvenceras

    end_time = time.perf_counter() # Reloj de ejecucion del programa
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time:.6f} segundos")

    return result # Retorna el resultado


b = int(input("Introduce una base: ")) # El usuario Introduce el valor de la base
e = int(input("Introduce un exponente: ")) # El usuario Introduce el valor del exponente
resultado = divideyvenceras(b, e) # Llama a la funcion principal
print("{} ^ {} = {}".format(b, e, resultado)) # Imprime el resultado
