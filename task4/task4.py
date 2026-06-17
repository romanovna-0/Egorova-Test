import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python task4.py <numbers_file>")
        return

    filepath = sys.argv[1]
    nums = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.strip():
                nums.append(int(line.strip()))

    if not nums:
        print(0)
        return

    nums.sort()
    n = len(nums)
    median = nums[n // 2]
    moves = sum(abs(x - median) for x in nums)

    if moves > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
    else:
        print(moves)

if __name__ == "__main__":
    main()
