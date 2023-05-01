# 행렬 곱셈 순서

import sys
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
# 중간중간 min 값 저장하는 dp, (2차원 배열에서 대각선 포함 오른쪽 위만 사용)
dp = [[0] * (n+1) for i in range(n+1)]

# 대각선 행렬 가까운 칸 부터 늘려감
# AB, BC, CD 검토하고 / min(ABC) min(BCD) 검토하고 / min(ABCD)
for i in range(1, n): #대각선 기준 몇 칸 떨어져 있는지
    for j in range(0, n-i):

        # AB, BC 등 차이 1칸 나는 경우
        if i == 1:
            dp[j][j+i] = a[j][0] * a[j][1] * a[j+1][1]

        # 1칸 이상 차이나는 경우 케이스 다 검토해서 min 값 찾아줌
        else:
            dp[j][j+i] = 2**32
            for k in range(j, j+i):
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + a[j][0] * a[k][1] * a[j+i][1])

print(dp[0][n-1])