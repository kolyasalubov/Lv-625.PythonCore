def distance(x1, y1, x2, y2):
    return float(f"{(abs(x1 - x2)**2 + abs(y1 - y2)**2)**0.5:.2f}")

print(distance(0,0,3,5))
