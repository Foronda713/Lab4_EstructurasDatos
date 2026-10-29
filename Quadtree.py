import math

class Punto:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def dist(self, p):
        return math.hypot(self.x - p.x, self.y - p.y)

class Rectangulo:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
    def contiene(self, p):
        return abs(p.x - self.x) <= self.w and abs(p.y - self.y) <= self.h
    def intersc_circulo(self, cx, cy, r):
        nx = max(self.x - self.w, min(cx, self.x + self.w))
        ny = max(self.y - self.h, min(cy, self.y + self.h))
        return math.hypot(cx - nx, cy - ny) <= r

class Quadtree:
    def __init__(self, boundary, cap=16):
        self.b, self.cap, self.pts, self.div = boundary, cap, [], False

    def subdivide(self):
        x, y, w, h = self.b.x, self.b.y, self.b.w / 2, self.b.h / 2
        self.nw = Quadtree(Rectangulo(x - w, y + h, w, h), self.cap)
        self.ne = Quadtree(Rectangulo(x + w, y + h, w, h), self.cap)
        self.sw = Quadtree(Rectangulo(x - w, y - h, w, h), self.cap)
        self.se = Quadtree(Rectangulo(x + w, y - h, w, h), self.cap)
        self.div = True

    def insertar(self, p):
        if not self.b.contiene(p): return False
        if len(self.pts) < self.cap and not self.div:
            self.pts.append(p)
            return True
        if not self.div:
            self.subdivide()
            for old in self.pts: self.ins_en_hijos(old)
            self.pts = []
        return self.ins_en_hijos(p)

    def ins_en_hijos(self, p):
        return self.ne.insertar(p) or self.nw.insertar(p) or self.se.insertar(p) or self.sw.insertar(p)

    def busca_radio(self, center, r, found=None):
        if found is None: found = []
        if not self.b.intersc_circulo(center.x, center.y, r): return found
        for p in self.pts:
            if center.dist(p) <= r: found.append(p)
        if self.div:
            for k in (self.nw, self.ne, self.sw, self.se): k.busca_radio(center, r, found)
        return found

    def vecino_cercano(self, center):
        r, res = 100, []
        while not res and r <= max(self.b.w, self.b.h) * 2:
            res = self.busca_radio(center, r)
            r *= 2
        return min(res, key=lambda p: center.dist(p)) if res else None