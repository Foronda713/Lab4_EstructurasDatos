import random
import matplotlib.pyplot as plt
from Quadtree import Punto, Rectangulo, Quadtree

random.seed(42)

# Generación de 10,000 puntos
pts = [Punto(random.uniform(0, 10000), random.uniform(0, 10000)) for _ in range(10000)]
qt = Quadtree(Rectangulo(5000, 5000, 5000, 5000))
for p in pts: 
    qt.insertar(p)

# Configuración de Búsqueda
centro, radio = Punto(7000, 3500), 700

# Verificaciones
bf_res = [p for p in pts if centro.dist(p) <= radio]
qt_res = qt.busca_radio(centro, radio)
assert len(bf_res) == len(qt_res), "Error en radio"

bf_vecino = min(pts, key=lambda p: centro.dist(p))
qt_vecino = qt.vecino_cercano(centro)
assert bf_vecino.dist(centro) == qt_vecino.dist(centro), "Error en vecino"
print("Pruebas pasadas!")

# ========================================================
# GRÁFICA 1: BÚSQUEDA POR RADIO (RANGE SEARCH)
# ========================================================
fig, ax = plt.subplots(figsize=(7, 7))

# Puntos generales de fondo
ax.scatter([p.x for p in pts], [p.y for p in pts], s=1, c='lightgray', alpha=0.4, label='Puntos de entrega')

# Puntos encontrados dentro del radio
ax.scatter([p.x for p in qt_res], [p.y for p in qt_res], s=8, c='crimson', label=f'Entregas en radio ({radio}m)')

# Punto central de consulta
ax.scatter([centro.x], [centro.y], s=60, c='blue', marker='X', zorder=5, label='Ubicación de consulta')

# Círculo del radio
circulo = plt.Circle((centro.x, centro.y), radio, fill=False, color='blue', linestyle='--', linewidth=1.5)
ax.add_patch(circulo)

# Configuración estética
ax.set_title(f"Verificación Visual: Entregas a {radio}m de Radio", fontsize=12, fontweight='bold', pad=12)
ax.set_xlabel("Coordenada X (metros)", fontsize=10)
ax.set_ylabel("Coordenada Y (metros)", fontsize=10)
ax.set_xlim(0, 10000)
ax.set_ylim(0, 10000)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.5)
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig("verificacion_radio.png", dpi=300)
plt.close()

# ========================================================
# GRÁFICA 2: VECINO MÁS CERCANO (1-NN)
# ========================================================
fig, ax = plt.subplots(figsize=(7, 7))

# Puntos de fondo
ax.scatter([p.x for p in pts], [p.y for p in pts], s=1, c='lightgray', alpha=0.4, label='Puntos de entrega')

# Punto de consulta
ax.scatter([centro.x], [centro.y], s=30, c='blue', marker='X', zorder=5, label='Ubicación de consulta')

# Vecino más cercano encontrado
ax.scatter([qt_vecino.x], [qt_vecino.y], s=15, c='forestgreen', marker='o', edgecolors='black', linewidth=0.8, zorder=6, label='Entrega más cercana')

# Línea de conexión
ax.plot([centro.x, qt_vecino.x], [centro.y, qt_vecino.y], color='forestgreen', linestyle=':', linewidth=1.5)

# Configuración estética
ax.set_title("Verificación Visual: Punto de Entrega Más Cercano", fontsize=12, fontweight='bold', pad=12)
ax.set_xlabel("Coordenada X (metros)", fontsize=10)
ax.set_ylabel("Coordenada Y (metros)", fontsize=10)
ax.set_xlim(0, 10000)
ax.set_ylim(0, 10000)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.5)
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig("verificacion_vecino_cercano.png", dpi=300)
plt.close()

# ========================================================
# GRÁFICA 3: K-VECINOS MÁS CERCANOS (K-NN, K=5)
# ========================================================
fig, ax = plt.subplots(figsize=(7, 7))

# Obtener los 5 vecinos más cercanos ordenando la lista
k = 50
k_vecinos = sorted(pts, key=lambda p: centro.dist(p))[:k]

# Puntos de fondo
ax.scatter([p.x for p in pts], [p.y for p in pts], s=1, c='lightgray', alpha=0.4, label='Puntos de entrega')

# Punto de consulta
ax.scatter([centro.x], [centro.y], s=30, c='blue', marker='X', zorder=5, label='Ubicación de consulta')

# Trazar líneas y puntos para cada uno de los K vecinos
for idx, vec in enumerate(k_vecinos):
    label_text = f'{k} Vecinos más cercanos' if idx == 0 else ""
    ax.scatter([vec.x], [vec.y], s=10, c='darkorange', marker='o', edgecolors='black', linewidth=0.8, zorder=6, label=label_text)
    ax.plot([centro.x, vec.x], [centro.y, vec.y], color='darkorange', linestyle='--', linewidth=1, alpha=0.8)

# Configuración estética
ax.set_title(f"Verificación Visual: {k} Vecinos Más Cercanos", fontsize=12, fontweight='bold', pad=12)
ax.set_xlabel("Coordenada X (metros)", fontsize=10)
ax.set_ylabel("Coordenada Y (metros)", fontsize=10)
ax.set_xlim(0, 10000)
ax.set_ylim(0, 10000)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.5)
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig("verificacion_k_vecinos.png", dpi=300)
plt.close()

print("✓ Guardadas: 'verificacion_radio.png', 'verificacion_vecino_cercano.png' y 'verificacion_k_vecinos.png'.")