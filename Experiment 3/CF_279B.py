n, t = map(int, input().split())
books = list(map(int, input().split()))

left = 0
current_sum = 0
best = 0

for right in range(n):
    current_sum += books[right]

    while current_sum > t:
        current_sum -= books[left]
        left += 1

    length = right - left + 1

    if length > best:
        best = length

print(best)
