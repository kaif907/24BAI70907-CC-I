n = int(input())
arr = list(map(int, input().split()))

ones = arr.count(1)

current = 0
best = -1

for x in arr:
    if x == 0:
        value = 1
    else:
        value = -1

    current += value

    if current > best:
        best = current

    if current < 0:
        current = 0

print(ones + best)
