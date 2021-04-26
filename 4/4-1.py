import sys

n = int(input())
road = sys.stdin.readline().split()
i,j = 1, 1

for item in road:
    if item == 'L':
        if j - 1 == 0:
            continue
        else:
            j -= 1
    elif item == 'R':
        if j + 1 > n:
            continue
        else:
            j += 1
    elif item == 'U':
        if i - 1 == 0:
            continue
        else:
            i -= 1
    elif item == 'D':
        if i + 1 > n:
            continue
        else:
            i += 1

print(i, j)
