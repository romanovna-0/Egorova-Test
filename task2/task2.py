import sys

file1 = open(sys.argv[1])
file2 = open(sys.argv[2])

x_center, y_center = map(float, file1.readline().split())
a, b = map(float, file1.readline().split())

for line in file2:
    x, y = map(float, line.split())
    value = ((x - x_center) / a) ** 2 + ((y - y_center) / b) ** 2
    if value < 1:
        print(1)
    elif value == 1:
        print(0)
    else:
        print(2)
