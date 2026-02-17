# Taller: Complejidad Algorítmica y Medición de Eficiencia

## 📋 Descripción
Este taller implementa y analiza algoritmos con diferentes complejidades temporales y espaciales, demostrando mediante mediciones prácticas las diferencias entre O(1), O(log n) y O(n).

## 🚀 Cómo Ejecutar el Código

### Requisitos Previos
- Python 3.x instalado
- Biblioteca `matplotlib` (para gráficas)

### Instalación de Dependencias
```bash
pip install matplotlib
```

### Ejecución
```bash
python taller_complejidad_.py
```

**Si usas entorno virtual:**
```bash
& ".venv\Scripts\python.exe" taller_complejidad_.py
```

### Menú Interactivo
El programa presenta un menú con las siguientes opciones:
1. Ejercicio 1.1 (Operaciones O(1))
2. Ejercicio 1.2 (Búsqueda Binaria)
3. Ejercicio 2.1 (Búsqueda Lineal)
4. Ejercicio 2.2 (Inserción en Orden)
5. Ejercicio 3.1 (Comparar Lineal vs Binaria)
6. Ejercicio 3.2 (Comparar Memoria)
7. Ejercicio 3.3 (Gráficas)
8. Ejecutar todo secuencialmente
0. Salir

---

## 📊 Conclusiones por Ejercicio

### **Ejercicio 1.1 - Operaciones O(1)**
**Complejidad:** O(1) en tiempo y espacio

**Conclusión:**  
Las operaciones aritméticas básicas (módulo `%`, comparaciones) son **constantes** independientemente del tamaño de los números. No requieren memoria adicional proporcional a la entrada.

**Operaciones implementadas:**
- ✓ Determinar si un número es par/impar
- ✓ Obtener el último dígito
- ✓ Encontrar el mayor entre dos números (sin usar `max()`)

---

### **Ejercicio 1.2 - Búsqueda Binaria O(log n)**
**Complejidad:** O(log n) en tiempo, O(1) en espacio

**Conclusión:**  
La búsqueda binaria **divide el espacio de búsqueda a la mitad** en cada iteración, resultando en un máximo de ⌈log₂(n)⌉ comparaciones. Para n=10,000 solo necesita ~14 comparaciones vs 10,000 de búsqueda lineal.

**Casos analizados:**
- **Mejor caso:** Elemento en el centro → 1 comparación
- **Peor caso:** Elemento no existe → log₂(n) comparaciones

**Ejemplo práctico:**
| n | log₂(n) | Comparaciones Peor Caso |
|---|---------|-------------------------|
| 100 | 6.6 | 7 |
| 1,000 | 10.0 | 10 |
| 10,000 | 13.3 | 14 |

---

### **Ejercicio 2.1 - Búsqueda Lineal**
**Complejidad:** O(n) en tiempo, O(1) en espacio

**Conclusión:**  
La búsqueda lineal recorre la lista secuencialmente. En el **mejor caso** (elemento al inicio) es O(1), pero en **promedio y peor caso** debe revisar ~n/2 o n elementos completos, resultando en **O(n)**.

**Casos demostrados (n=1000):**
- **Mejor caso:** Primera posición → 1 comparación
- **Caso promedio:** Mitad → 501 comparaciones
- **Peor caso:** No existe → 1000 comparaciones

**Ventaja:** Funciona con listas NO ordenadas.

---

### **Ejercicio 2.2 - Inserción en Orden**
**Complejidad:** O(n) en tiempo, O(1) en espacio

**Conclusión:**  
Insertar manteniendo el orden requiere:
1. **Buscar posición:** O(n) en búsqueda lineal
2. **Desplazar elementos:** O(n) en el peor caso (insertar al inicio)

**Casos analizados (n=1000):**
- **Mejor caso:** Insertar al final → 0 desplazamientos (pero búsqueda sigue siendo O(n))
- **Peor caso:** Insertar al inicio → 1000 desplazamientos

---

### **Ejercicio 3.1 - Comparación: Lineal vs Binaria**
**Conclusión:**  
La búsqueda binaria es **órdenes de magnitud más rápida** que la lineal a medida que n crece.

**Mediciones de tiempo (peor caso):**
| n | Tiempo Lineal | Tiempo Binaria | Factor de Mejora |
|---|---------------|----------------|------------------|
| 1,000 | ~0.04 ms | ~0.0003 ms | ~133x más rápida |
| 10,000 | ~0.40 ms | ~0.0004 ms | ~1,000x más rápida |
| 100,000 | ~4.00 ms | ~0.0005 ms | ~8,000x más rápida |

**Por qué:** O(log n) crece logarítmicamente vs O(n) que crece linealmente.  
**Requisito:** Búsqueda binaria requiere lista **ordenada**.

---

### **Ejercicio 3.2 - Memoria: Lista vs Generador**
**Conclusión:**  
Los **generadores** usan memoria **constante O(1)** independientemente de cuántos valores produzcan, mientras que las **listas** almacenan todos los elementos en memoria O(n).

**Medición práctica (n=1,000,000 cuadrados):**
- **Lista:** ~35-40 MB (almacena todos los valores)
- **Generador:** ~0.0001 MB (solo mantiene estado actual)

**Reducción:** ~400,000x menos memoria

**Cuándo usar generadores:**
- ✓ Procesar grandes volúmenes de datos
- ✓ Solo se necesita recorrer una vez
- ✓ Secuencias infinitas
- ✓ Procesamiento línea por línea de archivos

---

### **Ejercicio 3.3 - Visualización con Gráficas**
**Conclusión:**  
Las gráficas confirman visualmente el comportamiento teórico:

**Gráfica 1 (Tiempo):**  
Muestra crecimiento **lento y logarítmico** del tiempo de búsqueda binaria. Aunque hay fluctuaciones (normales en mediciones de tiempo), la tendencia es claramente O(log n).

**Gráfica 2 (Comparaciones):**  
Demuestra los **"escalones"** característicos porque log₂(n) produce valores discretos enteros. Cada escalón representa duplicar el tamaño de n, requiriendo solo una comparación adicional.

**Ejemplo:** 
- n=100→1000: crece de 7 a 10 comparaciones (+3)
- n=1000→10,000: crece de 10 a 14 comparaciones (+4)

Esto valida matemáticamente que la implementación es correcta.

---

## 🎯 Resumen General

### Complejidades Implementadas
| Algoritmo | Tiempo | Espacio | Mejor Caso | Peor Caso |
|-----------|--------|---------|------------|-----------|
| Operaciones O(1) | O(1) | O(1) | O(1) | O(1) |
| Búsqueda Binaria | O(log n) | O(1) | O(1) | O(log n) |
| Búsqueda Lineal | O(n) | O(1) | O(1) | O(n) |
| Inserción en Orden | O(n) | O(1) | O(n) | O(n) |
| Lista (cuadrados) | O(n) | **O(n)** | - | - |
| Generador (cuadrados) | O(1) | **O(1)** | - | - |

### Lecciones Clave
1. **O(1)** - Operaciones instantáneas, no dependen del tamaño de entrada
2. **O(log n)** - Crece muy lentamente, ideal para búsquedas en datos ordenados
3. **O(n)** - Crece linealmente, aceptable para conjuntos pequeños o una pasada
4. **Espacio vs Tiempo** - A veces se sacrifica memoria por velocidad, o viceversa
5. **Requisitos** - Algoritmos eficientes como búsqueda binaria requieren precondiciones (datos ordenados)

---

## 📚 Herramientas Utilizadas
- **`time.perf_counter()`** - Medición precisa de tiempo
- **`timeit.timeit()`** - Mediciones repetidas para promediar
- **`tracemalloc`** - Monitoreo de uso de memoria
- **`matplotlib`** - Visualización de resultados
