# 점프 (동적프로그래밍)

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n번째 돌 도착, m개의 small_stone
small_stone = [int(input()) for i in range(m)] # small_stone 리스트

dp = [[10001] * (int((2*n)**0.5) + 2) for i in range(n+1)]
dp[1][0] = 0  #[위치][속도]별 최소 점프 횟수 dp에 저장

# 각각의 n번째 돌에 대하여, 현재 속도별 최선의 case 검토 하여 dp에 저장
for i in range(2, n+1):
    # 못 머무는 돌이면 스킵
    if i in small_stone:
        continue
    # 현재 속도j별로, -j 돌에서 속도가 j-1, j, j+1 3가지 중 최솟값 + 1 (점프해서 i로 올 수 있는 3가지 케이스)
    for j in range(1, int((2*i)**0.5) + 1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

# 도착 못하면 -1 출력 / n번째 돌에서 최소 점프로 도착한 값 출력
if min(dp[n]) == 10001:
    print(-1)
else:
    print(min(dp[n]))