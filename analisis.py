import time
import random
import matplotlib.pyplot as plt
from Quadtree import Punto, Rectangulo, Quadtree

tamaños = [100, 500, 1000, 3000, 5000, 7000, 9000, 10000]

# Listas para los tiempos radio
t_radio_bf, t_radio_qt = [], []

# Listas para los tiempos vecino
t_vecino_bf, t_vecino_qt = [], []

centro = Punto(5000, 5000)
radio = 500
repeticiones = 30  # Promedio para evitar ruido

random.seed(42)

for N in tamaños:
    pts = [Punto(random.uniform(0, 10000), random.uniform(0, 10000)) for _ in range(N)]
    qt = Quadtree(Rectangulo(5000, 5000, 5000, 5000))
    for p in pts: 
        qt.insertar(p)

    # ----------------------------------------------------
    # Búsqueda por Radio
    # ----------------------------------------------------
    # Fuerza Bruta
    t0 = time.time()
    for _ in range(repeticiones):
        _ = [p for p in pts if centro.dist(p) <= radio]
    t_radio_bf.append((time.time() - t0) / repeticiones)

    # Quadtree
    t0 = time.time()
    for _ in range(repeticiones):
        _ = qt.busca_radio(centro, radio)
    t_radio_qt.append((time.time() - t0) / repeticiones)

    # ----------------------------------------------------
    # Vecino Cercano
    # ----------------------------------------------------
    # Fuerza Bruta
    t0 = time.time()
    for _ in range(repeticiones):
        _ = min(pts, key=lambda p: centro.dist(p))
    t_vecino_bf.append((time.time() - t0) / repeticiones)

    # Quadtree
    t0 = time.time()
    for _ in range(repeticiones):
        _ = qt.vecino_cercano(centro) if hasattr(qt, 'vecino_cercano') else qt.vecino_cercano(centro)
    t_vecino_qt.append((time.time() - t0) / repeticiones)


# ========================================================
# FIGURA 1: Radio (Escala Lineal)
# ========================================================
plt.figure(figsize=(8, 5))
plt.plot(tamaños, t_radio_bf, label='Fuerza Bruta O(N)', color='crimson', marker='o', linewidth=2)
plt.plot(tamaños, t_radio_qt, label='Quadtree O(log N)', color='royalblue', marker='s', linewidth=2)

plt.title('Rendimiento: Búsqueda por Radio (500m)', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Cantidad de Puntos de Entrega (N)', fontsize=10)
plt.ylabel('Tiempo promedio por consulta (segundos)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("comparativa_radio.png", dpi=300)
plt.close()

# ========================================================
# FIGURA 1B: Radio (Escala Logarítmica)
# ========================================================
plt.figure(figsize=(8, 5))
plt.plot(tamaños, t_radio_bf, label='Fuerza Bruta O(N)', color='crimson', marker='o', linewidth=2)
plt.plot(tamaños, t_radio_qt, label='Quadtree O(log N)', color='royalblue', marker='s', linewidth=2)

plt.yscale('log')  # Escala logarítmica en el eje Y
plt.title('Rendimiento: Búsqueda por Radio (Escala Logarítmica)', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Cantidad de Puntos de Entrega (N)', fontsize=10)
plt.ylabel('Tiempo promedio por consulta (segundos - Escala Log)', fontsize=10)
plt.grid(True, which="both", linestyle='--', alpha=0.6)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("comparativa_radio_log.png", dpi=300)
plt.close()


# ========================================================
# FIGURA 2: Vecino Cercano (Escala Lineal)
# ========================================================
plt.figure(figsize=(8, 5))
plt.plot(tamaños, t_vecino_bf, label='Fuerza Bruta O(N)', color='crimson', marker='o', linewidth=2)
plt.plot(tamaños, t_vecino_qt, label='Quadtree O(log N)', color='forestgreen', marker='^', linewidth=2)

plt.title('Rendimiento: Punto de Entrega Más Cercano', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Cantidad de Puntos de Entrega (N)', fontsize=10)
plt.ylabel('Tiempo promedio por consulta (segundos)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("comparativa_vecino.png", dpi=300)
plt.close()

# ========================================================
# FIGURA 2B: Vecino Cercano (Escala Logarítmica)
# ========================================================
plt.figure(figsize=(8, 5))
plt.plot(tamaños, t_vecino_bf, label='Fuerza Bruta O(N)', color='crimson', marker='o', linewidth=2)
plt.plot(tamaños, t_vecino_qt, label='Quadtree O(log N)', color='forestgreen', marker='^', linewidth=2)

plt.yscale('log')  # Escala logarítmica en el eje Y
plt.title('Rendimiento: Punto Más Cercano (Escala Logarítmica)', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Cantidad de Puntos de Entrega (N)', fontsize=10)
plt.ylabel('Tiempo promedio por consulta (segundos - Escala Log)', fontsize=10)
plt.grid(True, which="both", linestyle='--', alpha=0.6)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("comparativa_vecino_log.png", dpi=300)
plt.close()

print("✓ Guardadas: 'comparativa_radio.png', 'comparativa_radio_log.png', 'comparativa_vecino.png' y 'comparativa_vecino_log.png'.")