n, m = map(int, input().split())

moves = min(n, m)

winner = "Akshat"

if moves % 2 == 0:
    winner = "Malvika"

print(winner)
