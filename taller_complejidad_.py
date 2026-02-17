import time
import timeit
import tracemalloc
import math


TAMANOS_BINARIA = [100, 1000, 10000]
TAMANOS_COMPARA = [1000, 10000, 100000]
TAMANOS_GRAF = range(200, 20001, 800)


# --- Parte 1: Complejidad O(1) y O(log n) ---

def ejercicio_1_1(n, a, b):
    """
    Ejercicio 1.1 - Operaciones O(1)
    Escribe un programa que, dado un número n, haga solo operaciones de tiempo O(1) para:
    - Decidir si n es par o impar
    - Obtener el último dígito de n
    - Devolver el mayor entre dos números a y b (sin usar max())
    """
    print("\n--- Ejercicio 1.1: Operaciones O(1) ---")
    
    # Decidir si n es par o impar
    # Es O(1) porque el costo de la operación módulo (%) es constante independientemente de la magnitud de n
    # Espacio: O(1) ya que no se requiere memoria adicional proporcional a n
    # Razón: La operación módulo (%) es una operación aritmética básica que se ejecuta
    # en tiempo constante, independientemente del valor de n.
    es_paridad = n % 2 == 0
    print(f"¿{n} es par?: {es_paridad}")

    # Obtener el último dígito de n
    # Es O(1) porque realizar el módulo 10 toma un tiempo constante. Espacio: O(1).
    # Razón: La operación módulo 10 es aritmética simple que toma tiempo constante,
    # sin importar cuán grande sea n.
    digito_final = n % 10
    print(f"Último dígito de {n}: {digito_final}")

    # Devolver el mayor entre dos números a y b (sin max)
    # Es O(1) porque una sola comparación lógica toma tiempo constante. Espacio: O(1).
    # Razón: Solo hace una comparación simple y una asignación condicional,
    # ambas operaciones de tiempo constante.
    if a > b:
        maximo = a
    else:
        maximo = b
    print(f"El mayor entre {a} y {b} es: {maximo}")


def busqueda_binaria(lista, objetivo):
    """
    Ejercicio 1.2 - Búsqueda binaria O(log n)
    Implementa búsqueda binaria en una lista ordenada de enteros.
    
    Implementación de búsqueda binaria que retorna (indice, comparaciones).
    Complejidad Temporal: O(log n)
    Complejidad Espacial: O(1)
    
    Razón: En cada iteración se divide el espacio de búsqueda a la mitad,
    lo que resulta en un máximo de log₂(n) iteraciones.
    """
    bajo = 0
    alto = len(lista) - 1
    comparaciones = 0
    
    while bajo <= alto:
        comparaciones += 1
        medio = (bajo + alto) // 2
        valor_medio = lista[medio]
        
        if valor_medio == objetivo:
            return medio, comparaciones
        elif valor_medio < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
            
    return -1, comparaciones


def ejercicio_1_2():
    """
    Mide el número de comparaciones y comprueba que crece como O(log n).
    """
    print("\n--- Ejercicio 1.2: Búsqueda Binaria (O(log n)) ---")
    
    tamanos_prueba = TAMANOS_BINARIA
    for tam in tamanos_prueba:
        datos = list(range(tam))
        
        # Mejor caso: elemento en el centro
        indice_medio = tam // 2
        _, comp_mejor = busqueda_binaria(datos, datos[indice_medio])
        
        # Peor caso: elemento no está
        _, comp_peor = busqueda_binaria(datos, -1)
        
        print(f"Tam n={tam} | Mejor caso comps: {comp_mejor} | Peor caso comps: {comp_peor} (log2({tam}) ≈ {round(math.log2(tam), 1)})")


# --- Parte 2: Mejor, promedio y peor caso ---

def busqueda_lineal(lista, objetivo):
    """
    Ejercicio 2.1 - Búsqueda lineal (mejor, promedio y peor caso)
    Implementa búsqueda lineal (recorrer la lista de inicio a fin hasta encontrar el valor).
    
    Implementación de búsqueda lineal que retorna (indice, comparaciones).
    
    Complejidad en tiempo:
    - Mejor caso: O(1) - el elemento está en la primera posición
    - Caso promedio: O(n) - el elemento está en posición intermedia
    - Peor caso: O(n) - el elemento no existe o está al final
    
    Complejidad en espacio: O(1) - no usa memoria adicional
    """
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == objetivo:
            return i, comparaciones
    return -1, comparaciones


def ejercicio_2_1():
    """
    Para una lista de tamaño n y un valor a buscar:
    - Mejor caso: el valor está en la primera posición
    - Caso promedio: el valor está (por ejemplo) en la mitad  
    - Peor caso: el valor no está o está en la última posición
    """
    print("\n--- Ejercicio 2.1: Búsqueda Lineal ---")
    tam = 1000
    datos = list(range(tam))
    
    # Mejor caso
    _, comp_mejor = busqueda_lineal(datos, datos[0])
    print(f"Mejor caso (primera pos): {comp_mejor} comparaciones. O(1)")
    
    # Caso promedio
    _, comp_promedio = busqueda_lineal(datos, datos[tam // 2])
    print(f"Caso promedio (mitad): {comp_promedio} comparaciones. O(n)")
    
    # Peor caso
    _, comp_peor = busqueda_lineal(datos, -1)
    print(f"Peor caso (no está): {comp_peor} comparaciones. O(n)")


def insertar_en_orden(lista, nuevo_valor):
    """
    Ejercicio 2.2 - Inserción en orden
    
    Inserta un valor manteniendo el orden.
    Retorna el número de desplazamientos (simulados por la posición de inserción).
    Complejidad Peor Caso: O(n) debido a que list.insert(0, val) desplaza todos los elementos.
    
    Mejor caso: insertar al final - O(1) para inserción (pero O(n) para buscar posición)
    Peor caso: insertar al inicio - O(n) por desplazamientos
    """
    pos_insercion = len(lista)
    # Buscamos la posición de inserción (O(n) búsqueda lineal)
    for i in range(len(lista)):
        if lista[i] > nuevo_valor:
            pos_insercion = i
            break
            
    # La inserción desplaza (len(lista) - posicion) elementos
    movimientos = len(lista) - pos_insercion
    lista.insert(pos_insercion, nuevo_valor)
    return movimientos


def ejercicio_2_2():
    print("\n--- Ejercicio 2.2: Inserción en Orden ---")
    tam = 1000
    
    # Mejor caso: insertar al final
    lista_1 = list(range(tam))
    desp_mejor = insertar_en_orden(lista_1, tam + 1)
    print(f"Mejor caso (al final): {desp_mejor} desplazamientos. O(1) de inserción si es al final (pero buscar pos es O(n)).")

    # Peor caso: insertar al inicio
    lista_2 = list(range(tam))
    desp_peor = insertar_en_orden(lista_2, -1)
    print(f"Peor caso (al inicio): {desp_peor} desplazamientos. O(n)")


# --- Parte 3: Medición y comparación de eficiencia ---

def ejercicio_3_1():
    """
    Ejercicio 3.1 - Comparar búsqueda lineal vs binaria
    
    Usa listas ordenadas de distintos tamaños (por ejemplo 1000, 10000, 100000).
    Para cada tamaño, mide el tiempo de:
    - Búsqueda lineal (buscar un elemento que esté al final o no exista)
    - Búsqueda binaria (buscar el mismo tipo de elemento)
    
    Muestra una tabla: tamaño n, tiempo lineal (ms), tiempo binaria (ms), y una conclusión
    sobre cuál es más eficiente y por qué (O(n) vs O(log n)).
    """
    print("\n--- Ejercicio 3.1: Comparar Búsqueda Lineal vs. Binaria ---")
    tamanos_prueba = TAMANOS_COMPARA
    print(f"{'n':>10} | {'Lineal (ms)':>15} | {'Binaria (ms)':>15}")
    print("-" * 50)
    
    for tam in tamanos_prueba:
        datos = list(range(tam))
        buscado = -1  # Peor caso para ambas
        
        # Medir Lineal
        t0 = time.perf_counter()
        for _ in range(10):  # Promediar sobre 10 ejecuciones
            busqueda_lineal(datos, buscado)
        t1 = time.perf_counter()
        tiempo_lineal = ((t1 - t0) / 10) * 1000
        
        # Medir Binaria
        t0 = time.perf_counter()
        for _ in range(100):  # Binaria es muy rápida, promediamos más
            busqueda_binaria(datos, buscado)
        t1 = time.perf_counter()
        tiempo_binaria = ((t1 - t0) / 100) * 1000
        
        print(f"{tam:10d} | {tiempo_lineal:15.4f} | {tiempo_binaria:15.6f}")

    print("\nConclusión: La búsqueda binaria O(log n) es órdenes de magnitud más rápida que la lineal O(n) a medida que n crece.")


def ejercicio_3_2():
    """
    Ejercicio 3.2 - Comparar uso de memoria: Lista vs Generador
    
    Crea dos formas de representar "los primeros n cuadrados":
    1. Una lista: [1**2, 2**2, 3**2, ..., n**2]
    2. Un generador que devuelve esos mismos valores (uno a uno)
    
    Usa tracemalloc para medir la memoria usada al construir la lista y al "consumir" todo el generador.
    Para n grande (por ejemplo 100000 o 1000000), muestra:
    - memoria con lista (MB)
    - memoria con generador (MB)
    - conclusión (O(n) vs O(1) en espacio para la estructura)
    
    LISTA: almacena todos los elementos en memoria (O(n) espacio)
    GENERADOR: produce valores uno a uno (O(1) espacio)
    """
    print("\n--- Ejercicio 3.2: Comparar Uso de Memoria (Lista vs Generador) ---")
    tam = 1000000
    
    # Memoria para Lista
    # Complejidad en espacio: O(n) - La lista almacena todos los n elementos en memoria simultáneamente
    tracemalloc.start()
    lista_cuadrados = [i**2 for i in range(tam)]
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memoria_lista = peak / (1024 * 1024)
    
    # Memoria para Generador (al crearlo)
    # Complejidad en espacio: O(1) - El generador produce valores uno a uno
    # Solo mantiene el estado actual (un valor a la vez), no almacena toda la secuencia en memoria
    tracemalloc.start()
    gen_cuadrados = (i**2 for i in range(tam))
    current, peak = tracemalloc.get_traced_memory()
    # Consumir generador no debería aumentar memoria drásticamente si no guardamos todo
    for _ in gen_cuadrados:
        pass
    tracemalloc.stop()
    memoria_gen = peak / (1024 * 1024)

    print(f"n = {tam}")
    print(f"Memoria con Lista: {memoria_lista:.2f} MB")
    print(f"Memoria con Generador: {memoria_gen:.6f} MB")
    print("Conclusión: El generador usa O(1) de espacio adicional (memoria constante), mientras que la lista usa O(n).")


def ejercicio_3_3():
    """
    Ejercicio 3.3 - Generando Gráficas
    
    Genera gráficas que visualizan el comportamiento de la búsqueda binaria:
    - Tiempo de ejecución vs tamaño de lista
    - Número de comparaciones vs tamaño de lista
    """
    print("\n--- Ejercicio 3.3: Generando Gráficas ---")
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Error: matplotlib no está instalado. No se pueden generar gráficas.")
        return

    tamanos = TAMANOS_GRAF
    tiempos_binaria = []
    comparaciones_peor = []

    for tam in tamanos:
        datos = list(range(tam))
        # Medir tiempo binaria
        t = timeit.timeit(lambda: busqueda_binaria(datos, -1), number=1000)
        tiempos_binaria.append(t)
        
        # Comparaciones peor caso
        _, comp = busqueda_binaria(datos, -1)
        comparaciones_peor.append(comp)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Gráfica de Tiempo
    ax1.plot(tamanos, tiempos_binaria, marker='o', color='blue')
    ax1.set_title("Tiempo de Búsqueda Binaria (O(log n))")
    ax1.set_xlabel("Tamaño de la lista (n)")
    ax1.set_ylabel("Tiempo total (s) para 1000 runs")
    ax1.grid(True)

    # Gráfica de Comparaciones
    ax2.plot(tamanos, comparaciones_peor, marker='s', color='red')
    ax2.set_title("Comparaciones en Peor Caso (log2 n)")
    ax2.set_xlabel("n")
    ax2.set_ylabel("Número de comparaciones")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()


# --- Menú principal ---

def ejecutar_todo():
    ejercicio_1_1(10, 5, 8)
    ejercicio_1_2()
    ejercicio_2_1()
    ejercicio_2_2()
    ejercicio_3_1()
    ejercicio_3_2()
    ejercicio_3_3()


def menu():
    opciones = {
        "1": lambda: ejercicio_1_1(10, 5, 8),
        "2": ejercicio_1_2,
        "3": ejercicio_2_1,
        "4": ejercicio_2_2,
        "5": ejercicio_3_1,
        "6": ejercicio_3_2,
        "7": ejercicio_3_3,
        "8": ejecutar_todo,
    }

    while True:
        print("\n=== TALLER DE COMPLEJIDAD ALGORÍTMICA ===")
        print("1. Ejercicio 1.1 (O(1))")
        print("2. Ejercicio 1.2 (Búsqueda Binaria)")
        print("3. Ejercicio 2.1 (Búsqueda Lineal)")
        print("4. Ejercicio 2.2 (Inserción en Orden)")
        print("5. Ejercicio 3.1 (Comparar Lineal vs Binaria)")
        print("6. Ejercicio 3.2 (Comparar Memoria)")
        print("7. Ejercicio 3.3 (Gráficas)")
        print("8. Ejecutar todo secuencialmente")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            break

        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
