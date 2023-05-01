# 가장 긴 증가하는 부분수열

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [0 for i in range(n)]
# 자기자신보다 작은수중 '가장 큰 누적 수열길이 +1' 을 dp에 계속 저장
for i in range(n):
    # 본인 앞에 배열 모두 검사
    for j in range(i):
        if a[i] > a[j] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
