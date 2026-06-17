import sys

def build_path(n, m):
    index = 0
    path = []
    while True:
        path.append(str(index + 1))
        index = (index + m - 1) % n
        if index == 0:
            break
    return ''.join(path)

n1, m1, n2, m2 = map(int, sys.argv[1:5])
print(build_path(n1, m1) + build_path(n2, m2))