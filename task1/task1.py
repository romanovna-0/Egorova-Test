import sys

def get_path(n, m):
    arr = list(range(1, n + 1))
    index = 0
    path = []
    while True:
        path.append(arr[index])
        index = (index + m - 1) % n
        if index == 0:
            break
    return ''.join(map(str, path))

def main():
    if len(sys.argv) != 5:
        print("Usage: python task1.py n1 m1 n2 m2")
        return
    n1, m1, n2, m2 = map(int, sys.argv[1:5])
    result = get_path(n1, m1) + get_path(n2, m2)
    print(result)

if __name__ == "__main__":
    main()