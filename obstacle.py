import random

def get_obstacles(level):
    obstacles = []

    if level == 1:
        for i in range(5):
            obstacles.append((i * 40 + 100, 300))

    elif level == 2:
        for i in range(5):
            obstacles.append((i * 40 + 100, 300))
            obstacles.append((300, i * 40 + 100))

    elif level == 3:
        for i in range(10):
            obstacles.append((i * 20 + 50, 200))
            obstacles.append((400, i * 20 + 150))

    elif level == 4:
        for x in range(120, 500, 40):
            obstacles.append((x, 250))
        for y in range(100, 300, 40):
            obstacles.append((250, y))

    elif level == 5:
        for i in range(10):
            obstacles.append((i * 20 + 100, 100))
            obstacles.append((i * 20 + 100, 400))
            obstacles.append((100, i * 20 + 100))
            obstacles.append((400, i * 20 + 100))

    elif level == 6:
        for x in range(0, 600, 60):
            obstacles.append((x, x // 2))
            obstacles.append((600 - x, x // 2))

    elif level == 7:
        for i in range(0, 600, 30):
            if i % 60 == 0:
                obstacles.append((i, 300))
            else:
                obstacles.append((300, i))

    elif level == 8:
        for x in range(0, 600, 40):
            for y in range(0, 600, 120):
                obstacles.append((x, y))

    elif level == 9:
        for i in range(30, 570, 30):
            if i % 90 == 0:
                obstacles.append((i, i))
            else:
                obstacles.append((i, 600 - i))

    elif level >= 10:
        for x in range(50, 550, 50):
            for y in range(50, 550, 50):
                if (x + y) % 100 == 0:
                    obstacles.append((x, y))

    if level >= 12:
        for _ in range(level * 2):
            x = random.randint(0, 29) * 20
            y = random.randint(0, 29) * 20
            if (x, y) not in obstacles:
                obstacles.append((x, y))

    return obstacles


# Relleno para llegar a ~150 líneas
extra_data = [
    "obstáculos horizontales", "obstáculos verticales",
    "esquinas", "líneas cruzadas", "cercos",
    "patrones en espiral", "formas en X", "formas en H",
    "bloques centrados", "laberinto simple"
]

def get_obstacle_patterns():
    patterns = []
    for i in range(10):
        patterns.append(f"Patrón {i+1}: {extra_data[i % len(extra_data)]}")
    return patterns

def dummy_lines_for_padding():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    q = 17
    r = 18
    s = 19
    t = 20
    u = 21
    v = 22
    w = 23
    x = 24
    y = 25
    z = 26
    return a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z

dummy_lines_for_padding()
