# Laboratorio: Búsqueda Espacial Eficiente con Quadtree vs. Fuerza Bruta

**Estudiante:** Miguel Foronda  
**Materia:** Estructuras de Datos  
**Lenguaje:** Python 3.10+  

---

## Descripción del Proyecto

Este laboratorio aborda el problema de la logística urbana de entregas mediante la implementación desde cero de una estructura de datos espacial: un **Árbol Quadtree 2D**. El sistema procesa un mapa estático de $10.000$ puntos de entrega ($10\text{ km} \times 10\text{ km}$) para responder dos consultas críticas en tiempo real:

1. **Búsqueda por Radio (*Range Search*):** Identificar todos los puntos de entrega a $R$ metros de una ubicación dada.
2. **Vecino Más Cercano (*Nearest Neighbor*):** Encontrar el punto de entrega más próximo a un cliente.

El objetivo central es comparar experimentalmente la eficiencia del **Quadtree** frente al enfoque ingenuo de **Fuerza Bruta**, evaluando la reducción en tiempo de cómputo gracias a la poda de regiones del plano.

---

## Requerimientos Técnicos Implementados

1. **Estructura del Quadtree:**
   - **Nodo y Fronteras:** Representación mediante la clase `Rectangulo` (centro y semi-anchos) y descomposición jerárquica en 4 cuadrantes (`NW`, `NE`, `SW`, `SE`).
   - **Capacidad Fija:** Capacidad límite (`capacity = 16`) por nodo antes de subdividir el espacio de búsqueda.
2. **Poda Algorítmica :**
   - Inclusión del método geométrico `intersc_circulo` para descartar recursivamente subárboles enteros que no intersecan el radio de búsqueda.
3. **Búsqueda de Vecinos:**
   - Algoritmo de radio expansivo dinámico para la consulta del vecino más cercano ($1\text{-NN}$ y $K\text{-NN}$).
4. **Verificación Formal y Gráfica:**
   - Verificación de consistencia mediante `assert` comparando la exactitud del Quadtree frente a la Fuerza Bruta.
   - Generación automática de gráficos de dispersión (*scatter plots*) en Matplotlib.

---

## Nota sobre el Desarrollo y Metodología

El desarrollo de este laboratorio se realizó tomando como base conceptual y técnica el artículo (blog) de Lisyarus (*[Building a Quadtree](https://lisyarus.github.io/blog/posts/building-a-quadtree.html)*) y mediante un proceso de profundización asistido por Inteligencia Artificial (Gemini) para comprender a fondo el comportamiento interno del árbol. 

A través de la metodología de *Vibe Coding*, se realizaron iteraciones constantes con la IA para solucionar errores de refactorización, optimizar ciertas partes lógicas, documentar el código de forma clara y diseñar mejores visualizaciones gráficas.

---

## Estructura del Repositorio

El repositorio se compone de cuatro archivos principales:

```text
/
├── Imagenes/      # Carpeta con Imagenes de resultados obtenidos 
├── Quadtree.py    # Implementación desde cero (Punto, Rectangulo y Quadtree)
├── test.py        # Pruebas unitarias, aserciones y exportación de visualizaciones
├── analisis.py    # Benchmarking de rendimiento (escalas lineal y logarítmica)
└── README.md      # Informe y documentación del proyecto