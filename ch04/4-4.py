# 입력받기
n, m = map(int, input().split(' '))
x, y, news = map(int, input().split(' '))
maps = []
# 맵 생성
for _ in range(n):
    maps.append(list(map(int, input().split(' '))))
history = [(x, y)]

# 4방향을 다 보는지 체크
cnt = 0
while True:
    # 북쪽을 보고있다면
    if news == 0 and cnt != 4:
        # 만약 왼쪽방향이 땅이고 간적이 없다면
        if maps[x - 1][y] == 0 and (x - 1, y) not in history:
            # 방향 전환
            news += 1
            # 이동
            x -= 1
            # 이동한곳 기록 남기기
            history.append((x, y))
            cnt = 0
        # 만약 왼쪽방향이 바다거나 간적이 있다면
        else:
            # 방향 회전
            news += 1
            # 1번 탐방 4가 되면 끝
            cnt += 1
    elif news == 1 and cnt != 4:
        if maps[x][y + 1] == 0 and (x, y + 1) not in history:
            news += 1
            y += 1
            history.append((x, y))
            cnt = 0
        else:
            news += 1
            cnt += 1
    elif news == 2 and cnt != 4:
        if maps[x + 1][y] == 0 and (x + 1, y) not in history:
            news += 1
            x += 1
            history.append((x, y))
            cnt = 0
        else:
            news += 1
            cnt += 1
    elif news == 3 and cnt != 4:
        if maps[x][y - 1] == 0 and (x, y - 1) not in history:
            news = 0
            y -= 1
            history.append((x, y))
            cnt = 0
        else:
            news = 0
            cnt += 1
    # 4방향이 모두 이미 가본칸이거나 바다로 되어있는 경우
    if cnt == 4:
        # 북쪽이면
        if news == 0:
            # 만약 뒤로 가야하는 곳이 바다면
            if maps[x][y + 1] == 1:
                break
            # 아니면 남쪽으로 1칸 이동, 방향은 유지
            else:
                y += 1
        elif news == 1:
            if maps[x + 1][y] == 1:
                break
            else:
                x += 1
        elif news == 2:
            if maps[x][y - 1] == 1:
                break
            else:
                y -= 1
        elif news == 3:
            if maps[x - 1][y] == 1:
                break
            else:
                x -= 1
print(len(history))
