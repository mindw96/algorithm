n, m = map(int, input().split())
cards = []
min_temp = -1
for i in range(n):
    temp = list(map(int, input().split()))
    cards.append(temp)
    if min_temp < min(temp):
        min_temp = min(temp)

print(min_temp)
