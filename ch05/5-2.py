n, m = map(int, input().split(' '))
maze = []
for _ in range(n):
    maze.append(list(map(int, list(input()))))

count = 0

def dfs(x, y, count):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if maze[x][y] == 1:
        count += 1
        maze[x][y] = count

        dfs(x - 1, y, count)
        dfs(x + 1, y, count)
        dfs(x, y - 1, count)
        dfs(x, y + 1, count)

        return count
    return False


dfs(0, 0, count)
for i in range(n):
    for j in range(m):
        print(maze[i][j], end=' ')
    print()
print(maze[n-1][m-1])