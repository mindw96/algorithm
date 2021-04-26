import sys

n, m, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

answer = 0
cnt = 1

for _ in range(m):
    if cnt > k:
        answer += nums[-2]
        cnt = 1
        print(nums[-2])
    else:
        answer += nums[-1]
        cnt += 1
        print(nums[-1])

print(answer)