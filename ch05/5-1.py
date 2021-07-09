n, m = list(map(int, (input().split(' '))))
ice = []
for _ in range(n):
    ice.append(list(map(int, list(input()))))


def dfs(x, y):
    # x, y를 인덱스로 받고 만약 범위를 벗어나면 False 반환
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # ice 행렬 중 현재 위치의 값이 0이라면 (얼음 이라면)
    if ice[x][y] == 0:
        # 칸막이로 바꾸고
        ice[x][y] = 1
        # 현재 위치의 상하좌우를 모두 재귀호출하 근처의 모든 0을 1로 바꾼다
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
