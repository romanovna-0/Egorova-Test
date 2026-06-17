import sys
import math

def read_ellipse(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    x0, y0 = map(float, lines[0].split())
    a, b = map(float, lines[1].split())
    return x0, y0, a, b

def read_points(filepath):
    points = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.strip():
                x, y = map(float, line.split())
                points.append((x, y))
    return points

def main():
    if len(sys.argv) != 3:
        print("Usage: python task2.py <ellipse_file> <points_file>")
        return
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    x0, y0, a, b = read_ellipse(ellipse_file)
    points = read_points(points_file)

    eps = 1e-9
    for x, y in points:
        val = ((x - x0) ** 2) / (a ** 2) + ((y - y0) ** 2) / (b ** 2)
        if abs(val - 1.0) < eps:
            print(0)
        elif val < 1.0:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    main()