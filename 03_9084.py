# 동전 (동적프로그래밍)

import sys
t = int(sys.stdin.readline())  # t 테스트케이스

for i in range(t):
    n = int(sys.stdin.readline())
    # 동전(coins)은 오름차순으로 정렬되어 주어짐
    coins = list(map(int, sys.stdin.readline().split()))
    money = int(sys.stdin.readline())

    # memoization 하기 위한 배열
    dp = [0] * (money+1)
    dp[0] = 1

    # 동전 단위가 작은것 부터 다 검토
    for coin in coins:
        # j원 만들 수 있는 경우의 수 세어가며 올라감
        for j in range(money+1):
            if j >= coin:
                # 이번동전 'j-coin원' 만들 수 있는 경우의 수 + 기존동전 'j원' 만들 수 있는 경우의 수
                dp[j] += dp[j-coin]

    print(dp[money])
