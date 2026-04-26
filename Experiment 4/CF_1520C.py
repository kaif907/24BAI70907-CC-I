t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
        continue

    if n == 2:
        print(-1)
        continue

    nums = []

    for i in range(1, n*n + 1, 2):
        nums.append(i)

    for i in range(2, n*n + 1, 2):
        nums.append(i)

    index = 0

    for r in range(n):
        row = []
        for c in range(n):
            row.append(str(nums[index]))
            index += 1
        print(" ".join(row))
