n = int(input())

edges = []
deg = [0] * (n + 1)

for i in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))
    deg[u] += 1
    deg[v] += 1

special = -1

for i in range(1, n + 1):
    if deg[i] >= 3:
        special = i
        break

ans = [-1] * (n - 1)

if special == -1:
    for i in range(n - 1):
        ans[i] = i
else:
    label = 0

    for i in range(n - 1):
        u, v = edges[i]

        if (u == special or v == special) and label < 3:
            ans[i] = label
            label += 1

    for i in range(n - 1):
        if ans[i] == -1:
            ans[i] = label
            label += 1

for x in ans:
    print(x)
