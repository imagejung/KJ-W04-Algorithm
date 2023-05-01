# 평범한 배낭 (동적 프로그래밍)

import sys

n, k = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# 짐case는 첫번째 인덱스 (n번 돌면서 최대가치 찾기 위한 dp)
# weight는 배열의 두번째 인덱스, value는 배열의 값
dp = [[0] * (k+1) for i in range(n+1)]

# dp를 1차원 배열로 하면, 짐을 앞에서 하나 쓴뒤 본 배열이 바뀌어 버려 뒤에서 해당 짐을 안 썼을때 값을 모름...
for i in range(1,n+1):
    for j in range(k+1):
        w,v = a[i-1] # 짐 case 배열이 0부터 이므로 i-1
        if j >= w:
            # 2차원 배열로 해서 해당 i case 짐을 안썼을때의 기존 최대값 확인 (dp[i-1][j-w])
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])